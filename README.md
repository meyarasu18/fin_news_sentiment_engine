# AI-Powered Financial News & Sentiment Analysis Engine

## Overview

This project is an AI-powered application that analyzes financial news articles, determines sentiment (Positive, Negative, or Neutral), extracts important entities, predicts market impact, stores the results in a database, provides REST APIs using Flask, and visualizes insights using a Streamlit dashboard.

---

## Features

- Financial News Collection
- Text Preprocessing
- Sentiment Analysis using NLP
- Named Entity Extraction
- Market Impact Prediction
- SQLite Database Storage
- Flask REST API
- Streamlit Dashboard
- Interactive Charts
- CSV Data Processing

---

## Project Structure

```
financial_news_sentiment_engine/
│
├── api/
│   ├── __init__.py
│   └── routes.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── financial_news.csv
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── financial_news.db
│
├── entity/
│   ├── __init__.py
│   └── entity_extractor.py
│
├── news/
│   ├── __init__.py
│   └── news_collector.py
│
├── prediction/
│   ├── __init__.py
│   └── market_prediction.py
│
├── preprocessing/
│   ├── __init__.py
│   └── preprocess.py
│
├── sentiment/
│   ├── __init__.py
│   └── sentiment_model.py
│
├── utils/
│   ├── __init__.py
│   └── helper.py
│
├── outputs/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Technologies Used

- Python 3.11
- Flask
- Streamlit
- Pandas
- NumPy
- spaCy
- NLTK
- Transformers
- PyTorch
- Plotly
- SQLite

---

## Installation

### Clone the repository

```bash
git clone <repository_url>
cd financial_news_sentiment_engine
```

### Create Virtual Environment

```bash
py -3.11 -m venv venv
```

### Activate Virtual Environment

Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt

```cmd
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### Download NLTK Data

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
```

---

## Run Flask API

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /news | Get Financial News |
| GET | /sentiment | Sentiment Analysis |
| GET | /prediction | Market Predictions |
| GET | /company/<company_name> | Company Analysis |

---

## Workflow

```
Financial News
        │
        ▼
News Collection
        │
        ▼
Preprocessing
        │
        ▼
Sentiment Analysis
        │
        ▼
Entity Extraction
        │
        ▼
Market Impact Prediction
        │
        ▼
Database Storage
        │
        ├────────► Flask API
        │
        ▼
Streamlit Dashboard
```

---

## Sample Output

```
Company      : Apple

Headline     : Apple reports record quarterly earnings

Sentiment    : Positive

Confidence   : 98.45%

Impact       : High

Prediction   : Stock Price Likely to Increase
```

---

## Future Enhancements

- Live Financial News API Integration
- Real-Time Stock Price Analysis
- Deep Learning Sentiment Models
- Docker Deployment
- Cloud Deployment
- User Authentication
- Email Alerts
- Interactive Analytics Dashboard

---

## Author

**Meyarasu Subramani**

AI-Powered Financial News & Sentiment Analysis Engine
