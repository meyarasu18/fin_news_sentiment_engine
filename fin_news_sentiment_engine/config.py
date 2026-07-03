import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
MODEL_DIR = os.path.join(BASE_DIR, "models")

DATASET_PATH = os.path.join(DATA_DIR, "financial_news.csv")


DATABASE = os.path.join(BASE_DIR, "database", "financial_news.db")

HOST = "127.0.0.1"
PORT = 5000

STREAMLIT_PORT = 8501

LABELS = ["Positive", "Negative", "Neutral"]

CONFIDENCE_THRESHOLD = 0.70