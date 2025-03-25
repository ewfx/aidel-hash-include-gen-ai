import requests
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed
import os
import pandas as pd
from GoogleNews import GoogleNews
import re
from summarizer import Summarizer


class GoogleNewsSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn") -> None:
        self.summarizer = Summarizer(model_name=model_name)

    def get_news_article_links(self, company_list):
        query_string = " OR ".join(
            [f'"{company}"' for company in company_list])
        search_query = """({}) AND 
        ("financial anomaly" OR "financial irregularity" OR "regulatory filing" OR "legal action" OR 
        "financial fraud" OR "accounting fraud" OR "sanctions" OR "SEC investigation" OR "audit failure" OR 
        "class action lawsuit" OR "insider trading" OR "whistleblower complaint" OR "penalty" OR "fine" OR 
        "restatement" OR "regulatory scrutiny" OR "compliance violation" OR "litigation" OR 
        "shareholder lawsuit" OR "corporate governance violation" OR "misconduct" OR "stock manipulation")""".format(query_string)

        googlenews = GoogleNews(period='7d')
        googlenews.search(search_query)

        all_results = []
        for i in range(1, 10):
            googlenews.getpage(i)
            result = googlenews.result()
            if result:
                for item in result:
                    all_results.append(item)
                    if len(all_results) >= 10:
                        break

        df = pd.DataFrame(all_results)
        df = df.drop_duplicates(subset=['title'], keep='last')
        df.reset_index(drop=True, inplace=True)
        article_links = [re.split("&ved", link)[0] for link in df['link']]
        return article_links

    def fetch_description(self, url):
        try:
            # Attempt HTTP GET request
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "Referer": "https://www.google.com/",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive"
            }
            response = requests.get(url, timeout=10, headers=headers)
            if response.status_code == 200:
                html_content = response.text
            else:
                print(
                    f"Failed to retrieve: {url} (Status code: {response.status_code})")
                return "Failed to retrieve the webpage."

            # Parse HTML content if available
            if html_content:
                soup = BeautifulSoup(html_content, "html.parser")
                paragraphs = soup.find_all("p")
                page_description = " ".join([p.get_text() for p in paragraphs])
                return page_description
            else:
                return "Failed to retrieve the webpage."

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving {url}: {e}")
            return "Failed to retrieve the webpage."

    def fetch_all_descriptions(self, urls):
        """
        Fetch all descriptions concurrently using ProcessPoolExecutor
        """
        descriptions = []
        max_workers = max(1, os.cpu_count() - 1)

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_url = {executor.submit(
                self.fetch_description, url): url for url in urls}

            # Process results as they complete
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    descriptions.append(result)
                except Exception as e:
                    # print(f"Error processing {url}: {e}")
                    descriptions.append("Failed to retrieve the webpage.")
        print(f"Fetched {len(descriptions)} descriptions")
        return descriptions

    def get_summarized_news(self, company_list):
        news_article_links = self.get_news_article_links(company_list)
        consolidated_news_articles = self.fetch_all_descriptions(
            news_article_links)
        consolidated_news = " ".join(
            [articles for articles in consolidated_news_articles])
        summarized_news = self.summarizer.summarize_text(consolidated_news)
        return summarized_news
