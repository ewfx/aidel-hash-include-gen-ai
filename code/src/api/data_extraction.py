import requests
import json
from yahooquery import search, Ticker


class DataExtractor:

    def get_company_address(self, company_name, user_agent):
        """
        Function to get company address using OpenStreetMap
        """
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={company_name} headquarters"
        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                if data:
                    location = data[0]
                    full_address = location.get("display_name", "N/A")
                    country = location.get("address", {}).get("country", "N/A")
                    if country == "N/A" and "," in full_address:
                        country = full_address.split(",")[-1].strip()
                    return {
                        "Full Address": full_address,
                        "Country": country,
                        "Latitude": location.get("lat", "N/A"),
                        "Longitude": location.get("lon", "N/A"),
                    }
            except json.JSONDecodeError:
                print("OpenStreetMap API response error:", response.text)
        return {}

    def get_google_search_info(self, company_name, serpapi_key):
        """
        Function to get company info from Google Search (SerpAPI)
        """
        url = "https://serpapi.com/search"
        params = {"q": company_name, "api_key": serpapi_key}

        response = requests.get(url, params=params)
        if response.status_code == 200:
            try:
                data = response.json()
                if "knowledge_graph" in data:
                    kg = data["knowledge_graph"]
                    company_title = kg.get("title", "").strip()
                    if "See results about" in company_title:
                        company_title = company_name
                    return {
                        "Company Name": company_title,
                        "Headquarters": kg.get("headquarters", "N/A"),
                        "Website": kg.get("website", "N/A"),
                        "Description": kg.get("description", "N/A"),
                    }
            except json.JSONDecodeError:
                print("SerpAPI response error:", response.text)
        return {}

    def get_wikipedia_description(self, company_name):
        """
        Function to fetch company description from Wikipedia
        """
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{company_name}"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("extract", "N/A")
            except json.JSONDecodeError:
                print("Wikipedia API response error:", response.text)
        return "N/A"

    def get_yahoo_finance_data(self, company_name):
        """
        Function to fetch stock market data from Yahoo Finance
        """
        search_result = search(company_name)
        if not search_result or "quotes" not in search_result or not search_result["quotes"]:
            print(f"No stock symbol found for {company_name}")
            return {}

        first_result = search_result["quotes"][0]
        stock_symbol = first_result.get("symbol", "N/A")
        exchange_name = first_result.get("exchange", "N/A")

        ticker = Ticker(stock_symbol)

        # Ensure summary_detail is a dictionary
        summary = ticker.summary_detail.get(stock_symbol, {})
        if not isinstance(summary, dict):
            summary = {}

        # Ensure asset_profile is a dictionary
        asset_profile = ticker.asset_profile.get(stock_symbol, {})
        if not isinstance(asset_profile, dict):
            asset_profile = {}

        ceo_name = "N/A"
        if "companyOfficers" in asset_profile and isinstance(asset_profile["companyOfficers"], list):
            if len(asset_profile["companyOfficers"]) > 0:
                ceo_name = asset_profile["companyOfficers"][0].get(
                    "name", "N/A")

        return {
            "Stock Symbol": stock_symbol,
            "Market Cap": summary.get("marketCap", "N/A"),
            "Exchange": exchange_name,
            "Currency": summary.get("currency", "N/A"),
            "Industry": asset_profile.get("industry", "N/A"),
            "CEO": ceo_name,
            "Employees": asset_profile.get("fullTimeEmployees", "N/A"),
        }

    def check_sanctions_offshore(self, company_name):
        """
        Function to check company in sanctions/offshore databases
        """
        results = {}

        # OpenSanctions API
        opensanctions_url = f"https://api.opensanctions.org/match?query={company_name}"
        response = requests.get(opensanctions_url)
        if response.status_code == 200:
            results["OpenSanctions"] = response.json().get("results", [])

        # ICIJ Offshore Leaks Database
        icij_url = f"https://offshoreleaks.icij.org/search?q={company_name}"
        response = requests.get(icij_url)
        if response.status_code == 200:
            results["ICIJ Offshore"] = response.json().get("results", [])

        return results


def get_complete_company_info(self, company_name, serpapi_key, user_agent):
    """
    Function to get complete company information
    """
    google_info = self.get_google_search_info(company_name, serpapi_key)
    address_info = self.get_company_address(company_name, user_agent)
    finance_info = self.get_yahoo_finance_data(company_name)
    sanctions_info = self.check_sanctions_offshore(company_name)

    if google_info.get("Description", "N/A") == "N/A":
        google_info["Description"] = self.get_wikipedia_description(
            company_name)

    company_data = {**google_info, **address_info,
                    **finance_info, **sanctions_info}
    return company_data


# Example usage
serpapi_key = "GOOGLE_SERP_API_KEY"
user_agent = "your_email@example.com"
company_name = "Constellation Capital Corp."

company_details = get_complete_company_info(
    company_name, serpapi_key, user_agent)

for key, value in company_details.items():
    print(f"{key}: {value}")


def classify_entity_type(industry):

    shell_industries = {"Shell Companies", "Blank Check Company",
                        "Special Purpose Acquisition Company (SPAC)"}
    return "Shell Company" if industry in shell_industries else industry


def structure_company_data(company_details, transaction_id, confidence_score, sources_used):

    industry = company_details.get("Industry", "Unknown")
    entity_type = classify_entity_type(industry)

    return {
        "Transaction ID": transaction_id,
        "Extracted Entity": [company_details.get("Company Name", "Unknown")],
        # Dynamically assigns "Shell Company" if applicable
        "Entity Type": [entity_type],
        "Supporting Evidence": sources_used,  # Uses only sources that provided data
        "Confidence Score": confidence_score,
        "Reason": f"{company_details.get('Company Name', 'Unknown')} is categorized as "
                  f"{entity_type} with a company status of {company_details.get('Company Status', 'Unknown')}.",
    }


# Example usage:
company_details = {
    "Company Name": "Atlas Technology Group Inc.",
    "Industry": "Shell Companies",  # Industry that indicates a shell company
    "Company Status": "Active"
}

# Dynamically set the sources based on actual API usage
sources_used = ["Yahoo Finance", "SEC Filings"]
transaction_id = "TXN12345"
confidence_score = 0.95

structured_response = structure_company_data(
    company_details, transaction_id, confidence_score, sources_used)

# Print structured response
print(json.dumps(structured_response, indent=4))
