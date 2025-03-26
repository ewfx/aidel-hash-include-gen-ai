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
  - [🏗️ Tech Stack and Architecture:](#️-tech-stack-and-architecture)
  - [👥 Team](#-team)

---

## 🎯 Introduction

**AERIS (AI-Enabled Risk and Intelligence System)** is an AI-powered solution designed to analyze financial transactions, regulatory filings, news and other publicly available sources to predict _risk levels_ and provide _confidence-backed justifications_ using explainable AI.

With AERIS, we aim to empower financial analysts and compliance teams with an intelligent system that delivers accurate risk insights and improves decision-making.

## 🎥 Demo

🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration

The inspiration behind **AERIS** came from recognizing the challenges financial institutions face in identifying and mitigating risks efficiently. Traditional risk analysis processes are often manual, time-consuming, and prone to errors, making it difficult to detect emerging threats in real time.

With the exponential increase in financial data, including regulatory filings, financial news, and market trends, we realized that AI-driven solutions could bridge the gap by automating risk detection and providing explainable insights. Our goal was to build a system that not only flags potential risks but also explains the rationale behind those decisions to enhance transparency and trust.

## ⚙️ What It Does

**AERIS** (**AI-Enabled Risk and Intelligence System**) leverages **multi-model AI pipelines** to extract, analyze, and assess risks in financial data, providing accurate risk scores with detailed explanations. It combines **Natural Language Processing (NLP) models** with machine learning techniques to identify potential financial anomalies, compliance violations, and fraud from diverse sources.

### Key Functionalities

- **Data Aggregation:**  
   Fetches data from **Google News, Yahoo Finance, and SEC Filings APIs**, ensuring real-time updates on company performance, regulatory filings, and market sentiments.

- **Risk & Sentiment Analysis:**  
   Uses multiple models such as:

  - **SEC-BERT:** Analyzes 10K, 10Q, and 8K reports from the SEC for regulatory compliance and risks.
  - **FinBERT:** Conducts sentiment analysis on financial news to detect market sentiment.
  - **RoBERTa:** Evaluates compliance violations, insider trading patterns, and fraud detection.

- **Explainability:**  
   Used **SHAP and LIME** to explain the rationale behind risk scores, ensuring transparency in decision-making. It dynamically maps risks using a classification model trained on historical data.

- **Dynamic Risk Mapping:**  
   Assigns risk scores dynamically based on historical trends and domain-specific knowledge, ensuring a contextual understanding of financial risks.

---

## 🛠️ How We Built It

We built our solution by leveraging multiple AI models and APIs to create a robust and scalable risk analysis system.

---

## 🚧 Challenges We Faced

Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run

1. Clone the repository
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies
   ```sh
   npm install  # or pip install -r requirements.txt (for Python)
   ```
3. Run the project
   ```sh
   npm start  # or python app.py
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
- **LLM Models:**
  - **SEC-BERT:** For parsing and understanding SEC filings.
  - **FinBERT:** For sentiment analysis on financial data.
  - **RoBERTa:** For identifying high-risk entities and compliance violations.
  - **XGBoost:** For ensemble classification and risk prediction.
- **Explainability:** SHAP and LIME to Provide interpretability and explanations for model predictions.

---

## 👥 Team

- **Nirvik Agarwal** - [GitHub](#) | [LinkedIn](#)
- **Lakshetha T** - [GitHub](#) | [LinkedIn](#)
- **Kaushik S** - [GitHub](#) | [LinkedIn](#)
- **Chanukya Balli** - [GitHub](#) | [LinkedIn](#)
- **Shreeraj V. Bhamare** - [GitHub](#) | [LinkedIn](#)
