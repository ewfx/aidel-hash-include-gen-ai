
import re
import pandas as pd
from transformers import pipeline
import os
from fuzzywuzzy import fuzz

nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")


def parse_transaction_file(file_path):
    transactions, extension = process_file(file_path)
    processed_df = None
    file_type = ""
    json_data_list = []
    para_data_list = []
    if extension == ".txt":
        for j, transaction in enumerate(transactions):
            if is_json(transaction):
                results = extract_entities_json(transaction)
                data = {key: ', '.join(value)
                        for key, value in results.items()}
                json_data_list.append(data)
                df = pd.DataFrame(json_data_list)
                df.replace("", pd.NA, inplace=True)
                processed_df = df.dropna(axis=1, how='all')
                processed_df.to_csv('semi_structured.csv', index=False)
                file_type = "semistrcutured"
            else:
                results = process_text_by_category(transaction)
                data = {key: ', '.join(value)
                        for key, value in results.items()}
                para_data_list.append(data)
                processed_df = pd.DataFrame(para_data_list)
                processed_df.to_csv('unstructured.csv', index=False)
                file_type = "unstructured"
    else:
        processed_df = transactions
        file_type = "structured"
    return processed_df, file_type


def process_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".txt":
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        transactions = text.split("---")
    elif file_extension == ".csv":
        transactions = pd.read_csv(file_path)
    return transactions, file_extension


def is_json(text):
    structured_patterns = [
        r"Transaction ID:\s*\S+",
        r"Sender:\s*- Name:",
        r"Receiver:\s*- Name:",
        r"Amount:\s*\$?\d+",
    ]

    for pattern in structured_patterns:
        if re.search(pattern, text):
            return True
    return False


def extract_entities_json(text):
    entities = {}
    patterns = {
        "Transaction ID": r"Transaction ID:\s*(\S+)",
        "Date": r"Date:\s*([\d-]+ \d{2}:\d{2}:\d{2})",
        "Sender Name": r"Sender:\s*(?:- )?Name:\s*\"?([^\n\"]+)\"?",
        "Sender Account": r"Sender:.*?Account:\s*([\w\s\(\)-]+)",
        "Sender Address": r"Sender:.*?Address:\s*([^\n]+)",
        "Sender Beneficiary": r"Beneficiary Owner:\s*\"([^\"]+)\"",
        "Sender Notes": r"Sender:.*?Notes:\s*\"([^\"]+)\"",
        "Receiver Name": r"Receiver:\s*(?:- )?Name:\s*\"?([^\n\"]+)\"?",
        "Receiver Account": r"Receiver:.*?Account:\s*([\w\s\(\)-]+)",
        "Receiver Address": r"Receiver:.*?Address:\s*([^\n]+)",
        "Receiver Tax ID": r"Receiver:.*?Tax ID:\s*([\w-]+)",
        "Receiver Registration": r"Receiver:.*?Registration:\s*([^\n]+)",
        "Amount": r"Amount:\s*\$([\d,\.]+)",
        "Currency Exchange": r"Currency Exchange:\s*([^\n]+)",
        "Transaction Type": r"Transaction Type:\s*([^\n]+)",
        "Reference": r"Reference:\s*\"([^\"]+)\"",
        "Additional Notes": r'Additional Notes:\s*(?:-\s*\"([^\"]+)\"\s*)+'
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        entities[key] = [match.group(1) if match else ""]

    return entities


def process_text_by_category(text):
    combined = combine_entities(text)
    final_results = {}
    for category, ents in combined.items():
        clusters = cluster_entities(ents)
        final_results[category] = standardize_entities(clusters)
    return final_results


def combine_entities(text):
    spacy_ents = extract_model_entities_by_category(text)
    custom_ents = extract_custom_entities_by_category(text)

    combined = {}
    for category in ["ORG", "PERSON", "GPE", "MONEY"]:
        combined[category] = list(
            set(spacy_ents.get(category, []) + custom_ents.get(category, [])))
    return combined


def cluster_entities(entities, threshold=80):
    unique_entities = list(set(entities))
    clusters = {}

    while unique_entities:
        base = unique_entities.pop(0)
        group = [base]
        for entity in unique_entities[:]:
            if fuzz.ratio(base.lower(), entity.lower()) >= threshold:
                group.append(entity)
                unique_entities.remove(entity)
        clusters[base] = group

    return clusters


def standardize_entities(clusters):
    standardized = []
    for group in clusters.values():
        representative = max(group, key=len)
        standardized.append(representative)
    return standardized


def extract_model_entities_by_category(text):
    doc = nlp(text)
    result = {"ORG": [], "PERSON": [], "GPE": [], "MONEY": []}

    entity_map = {
        "I-ORG": "ORG",
        "I-PER": "PERSON",
        "I-LOC": "GPE",
        "I-MISC": "MONEY"
    }
    current_entity = ""
    current_label = ""
    prev_label = None

    for token in doc:
        entity = token["entity"]
        word = token["word"]
        if entity in entity_map:
            category = entity_map[entity]
            if word.startswith("##"):
                word = word[2:]
            if prev_label == entity:
                current_entity += " " + word
            else:
                if current_entity and current_label:
                    result[current_label].append(current_entity.strip())
                current_entity = word
                current_label = category
            prev_label = entity
        else:
            if current_entity and current_label:
                result[current_label].append(current_entity.strip())
            current_entity = ""
            current_label = ""
            prev_label = None
    if current_entity and current_label:
        result[current_label].append(current_entity.strip())
    for key in result:
        result[key] = clean_entities(list(set(result[key])))

    return result


def extract_custom_entities_by_category(text):
    result = {"ORG": [], "PERSON": []}
    pattern_blocked_person = re.compile(r"(Blocked Person [A-Z])")
    pattern_entity = re.compile(r"(Entity [A-Z])")

    matches_blocked_person = pattern_blocked_person.findall(text)
    matches_entity = pattern_entity.findall(text)

    result["PERSON"].extend(matches_blocked_person)
    result["ORG"].extend(matches_entity)

    for key in result:
        result[key] = list(set(result[key]))
    return result


def clean_entities(entities):
    cleaned_entities = []

    for entity in entities:
        entity = re.sub(r'\b[A-Z]\b', '', entity)
        entity = re.sub(r'\s+', ' ', entity).strip()
        words = entity.split()
        cleaned_entity = []
        for word in words:
            if len(word) > 1 or word in {"EU", "USD"}:
                cleaned_entity.append(word)
        cleaned_text = " ".join(cleaned_entity)
        if cleaned_text and cleaned_text not in cleaned_entities:
            cleaned_entities.append(cleaned_text)

    return cleaned_entities
