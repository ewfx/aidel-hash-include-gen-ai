# 🚀 AERIS – AI-Enabled Risk and Intelligence System

## 📌 Table of Contents

- [🚀 AERIS – AI-Enabled Risk and Intelligence System](#-aeris--ai-enabled-risk-and-intelligence-system)
  - [📌 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🎥 Demo](#-demo)
  - [💡 Inspiration](#-inspiration)
  - [⚙️ What It Does](#️-what-it-does)
    - [Key Functionalities](#key-functionalities)
  - [🛠️ How We Built It](#️-how-we-built-it)
  - [🚧 Challenges We Faced](#-challenges-we-faced)
  - [🏃 How to Run](#-how-to-run)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Backend Setup](#2-backend-setup)
    - [3. UI Setup](#3-ui-setup)
  - [🏗️ Tech Stack and Architecture:](#️-tech-stack-and-architecture)
  - [👥 Team](#-team)

---

## 🎯 Introduction

**AERIS (AI-Enabled Risk and Intelligence System)** is an AI-powered solution designed to analyze financial transactions, regulatory filings, news and other publicly available sources to predict _risk levels_ and provide _confidence-backed justifications_ using explainable AI.

With AERIS, we aim to empower financial analysts and compliance teams with an intelligent system that delivers accurate risk insights and improves decision-making.

## 🎥 Demo

🖼️ Screenshots:

![UI Interface](/artifacts/demo/UI%20Screenshots/UI%20Interface.png)
<br />
![Transactions Summary](/artifacts/demo/UI%20Screenshots/TransactionsSummary.png)

## 💡 Inspiration

The inspiration behind **AERIS** came from recognizing the challenges financial institutions face in identifying and mitigating risks efficiently. Traditional risk analysis processes are often manual, time-consuming, and prone to errors, making it difficult to detect emerging threats in real time.

With the exponential increase in financial data, including regulatory filings, financial news, and market trends, we realized that AI-driven solutions could bridge the gap by automating risk detection and providing explainable insights. Our goal was to build a system that not only flags potential risks but also explains the rationale behind those decisions to enhance transparency and trust.

## ⚙️ What It Does

**AERIS** (**AI-Enabled Risk and Intelligence System**) leverages **multi-model AI pipelines** to extract, analyze, and assess risks in financial data, providing accurate risk scores with detailed explanations. It combines **Natural Language Processing (NLP)** and **Large Language Models (LLMs)** to identify potential financial anomalies, compliance violations, and fraud from diverse sources.

### Key Functionalities

- **Data Aggregation:**  
   Fetches data from **Google News, Yahoo Finance, WikiData, and SEC Filings APIs**, ensuring real-time updates on company performance, regulatory filings, and market sentiments.

- **Risk & Sentiment Analysis:**  
   Uses multiple models such as:

  - **SEC-BERT:** Analyzes **10K, 10Q, and 8K** reports from the SEC for regulatory compliance and risks and provides the risk scores.
  - **FinBERT** and **RoBERTa**: Conducts sentiment analysis on financial news to detect market sentiment.

- **Explainability:**  
   Used **SHAP and LIME** to explain the rationale behind risk scores, ensuring transparency in decision-making. It dynamically maps risks using a classification model trained on historical data.

- **Dynamic Risk Mapping:**  
   Assigns risk scores dynamically based on historical trends and domain-specific knowledge, ensuring a contextual understanding of financial risks.

---

## 🛠️ How We Built It

We built our solution by leveraging multiple AI models and APIs to create a robust and scalable risk analysis system.

---

## 🚧 Challenges We Faced

- **Data Integration Complexity:**
  Needed to integrate multiple open datasets & APIs:
  - OpenStreetMap (company add.)
  - SerpAPI (google search)
  - Wikipedia (company desc)
  - Yahoo finance (market data)
  - OpenSanctions API
  - ICIJ Offshore Leaks
- Handling rate limits & API restrictions for different sources.

- **Unstructured Transaction Data:** Unstructured data (free-text transaction details) required extra processing & entity extraction.

- Lack of available data for Shell Companies

## 🏃 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ewfx/aidel-hash-include-gen-ai.git
cd aidel-hash-include-gen-ai
```

### 2. Backend Setup

```bash
# Create a virtual environment
cd code/src/api
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt

# Run Flask API
python app.py
```

### 3. UI Setup

```bash
# Make sure you are the root of the repository
cd code/src/ui

# Install React dependencies
npm install

# Run React frontend
npm start
```

## 🏗️ Tech Stack and Architecture:

- **Frontend:** ReactJS for a clean and intuitive user interface.
- **Backend:** Flask for building RESTful APIs and handling model inference.
- **Database:** MongoDB to store entity and risk data.
- **APIs / Data Sources:**
  - Google News
  - Yahoo Finance
  - SEC Filings
  - WikiData
  - OpenSanctions
  - OpenStreetMap
  - ICIJ Offshore Leaks
- **LLM Models:**
  - **bert-large-cased:** For Entity Extraction form Transaction Data
  - **SEC-BERT:** For parsing and understanding SEC filings.
  - **FinBERT:** For sentiment analysis on financial data.
  - **RoBERTa:** For identifying high-risk entities and compliance violations.
  - **XGBoost:** For ensemble classification and risk prediction.
- **Explainability:** SHAP and LIME to Provide interpretability and explanations for model predictions.

---

## 👥 Team

- **Nirvik Agarwal** - [GitHub](https://github.com/nirvikagarwal) | [LinkedIn](https://in.linkedin.com/in/nirvik-agarwal)
- **Lakshetha T** - [GitHub](https://github.com/lakshethaaa) | [LinkedIn](https://www.linkedin.com/in/lakshetha-t-99107a225/)
- **Kaushik S** - [GitHub](https://github.com/Kaushik1223) | [LinkedIn](https://www.linkedin.com/in/kaushik1223/)
- **Chanukya Balli** - [GitHub](https://github.com/Chanukya0426) | [LinkedIn](https://www.linkedin.com/in/balli-chanukya-52191123a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- **Shreeraj V. Bhamare** - [GitHub](https://github.com/shreerajbhamare) | [LinkedIn](https://www.linkedin.com/in/shreerajbhamare/)
