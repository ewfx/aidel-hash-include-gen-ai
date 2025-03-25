from sec_api import QueryApi
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import requests
from bs4 import BeautifulSoup


class SECRiskAnalyzer:

    def __init__(self, api_key) -> None:
        classification_model_name = "nlpaueb/sec-bert-base"
        tokenizer = AutoTokenizer.from_pretrained(classification_model_name)
        model = AutoModelForSequenceClassification.from_pretrained(
            classification_model_name)
        summary_model = "facebook/bart-large-cnn"
        self.summarizer = pipeline("summarization", model=summary_model)
        self.risk_classifier = pipeline(
            "text-classification", model=model, tokenizer=tokenizer)
        self.query_api = QueryApi(api_key=api_key)

    def extract_filing_content(self, url):
        """
        Extracts content from a given URL using BeautifulSoup.
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Host": "www.sec.gov",
            "Connection": "keep-alive",
        }
        try:
            response = requests.get(url, timeout=10, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Extract and clean all paragraph text from the document
                paragraphs = soup.find_all("p")
                content = " ".join([p.get_text().strip() for p in paragraphs])

                # If no paragraphs are found, fallback to all text
                if not content:
                    content = soup.get_text().strip()

                return content
            else:
                return "Failed to retrieve content."
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving {url}: {e}")
            return "Failed to retrieve content."

    def assess_risk_with_explanation(self, content):
        # Limit content length for SEC-BERT
        content_chunk = content[:1000]

        # Get risk classification result
        risk_result = self.risk_classifier(content_chunk)
        risk_label = risk_result[0]['label']
        risk_score = risk_result[0]['score']

        # Generate explanation for risk using summarizer
        summary_chunks = [content[i:i+2000]
                          for i in range(0, len(content), 2000)]
        summaries = [self.summarizer(chunk, max_length=150, min_length=50, do_sample=False)[
            0]['summary_text'] for chunk in summary_chunks]
        explanation = " ".join(summaries)

        return risk_label, risk_score, explanation

    def extract_and_summarize_reports(self, ticker):
        """
        Extracts SEC reports for a given company and report types,
        and summarizes them using a pre-trained summarizer model.
        """

        query = {
            "query": {
                "query_string": {
                    "query": f"ticker:{ticker} AND (formType:\"10-K\" OR formType:\"10-Q\" OR formType:\"8-K\") AND filedAt:[now-3y TO now]"
                }
            },
            "from": "0",  # Pagination start
            "size": "5",  # Limit to 5 filings
            # Sort by most recent filings
            "sort": [{"filedAt": {"order": "desc"}}],
        }

        response = self.queryApi.get_filings(query)

        filings = response["filings"]
        filings_data = []
        for filing in filings:
            filings_data.append({
                "company": filing.get("companyName", "N/A"),
                "ticker": filing.get("ticker", "N/A"),
                "form_type": filing.get("formType", "N/A"),
                "filed_date": filing.get("filedAt", "N/A"),
                "filing_url": filing.get("linkToFilingDetails", "N/A")
            })

        # Create DataFrame for easy viewing
        df = pd.DataFrame(filings_data)
        df['filing_content'] = df['filing_url'].apply(
            lambda x: self.extract_filing_content(x))
        df[['risk_label', 'risk_score', 'explanation']] = df['filing_content'].apply(
            lambda x: pd.Series(self.assess_risk_with_explanation(x))
        )

        # df[['company', 'form_type', 'filed_date', 'risk_label', 'risk_score', 'explanation', 'filing_url']].to_csv(
        #     "risk_analysis_with_explanations.csv", index=False
        # )
        # print(
        #     "Risk analysis with explanations saved to risk_analysis_with_explanations.csv")
        return df
