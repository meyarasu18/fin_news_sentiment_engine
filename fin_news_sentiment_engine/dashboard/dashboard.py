import streamlit as st
import pandas as pd
import plotly.express as px

from news.news_collector import NewsCollector
from sentiment.sentiment_model import SentimentAnalyzer
from prediction.market_prediction import MarketImpactPredictor

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Financial News Sentiment Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI-Powered Financial News & Sentiment Analysis Dashboard")
st.write("Analyze financial news and predict market impact.")

# -----------------------------
# Load Data
# -----------------------------
collector = NewsCollector()
df = collector.load_news()

# -----------------------------
# Analyze Sentiment
# -----------------------------
analyzer = SentimentAnalyzer()
predictor = MarketImpactPredictor()

results = []

for _, row in df.iterrows():

    sentiment_result = analyzer.analyze(row["headline"])

    prediction = predictor.predict(
        row["headline"],
        sentiment_result["sentiment"]
    )

    results.append({
        "Company": row["company"],
        "Sector": row["sector"],
        "Headline": row["headline"],
        "Sentiment": sentiment_result["sentiment"],
        "Confidence": round(sentiment_result["confidence"], 2),
        "Impact": prediction["impact"],
        "Prediction": prediction["prediction"]
    })

result_df = pd.DataFrame(results)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

companies = ["All"] + sorted(result_df["Company"].unique().tolist())
selected_company = st.sidebar.selectbox(
    "Select Company",
    companies
)

sentiments = ["All"] + sorted(result_df["Sentiment"].unique().tolist())
selected_sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    sentiments
)

filtered_df = result_df.copy()

if selected_company != "All":
    filtered_df = filtered_df[
        filtered_df["Company"] == selected_company
    ]

if selected_sentiment != "All":
    filtered_df = filtered_df[
        filtered_df["Sentiment"] == selected_sentiment
    ]

# -----------------------------
# Metrics
# -----------------------------
st.subheader("Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total News", len(filtered_df))
col2.metric(
    "Positive",
    (filtered_df["Sentiment"] == "Positive").sum()
)
col3.metric(
    "Negative",
    (filtered_df["Sentiment"] == "Negative").sum()
)
col4.metric(
    "Neutral",
    (filtered_df["Sentiment"] == "Neutral").sum()
)

# -----------------------------
# News Table
# -----------------------------
st.subheader("Financial News Analysis")

st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# Sentiment Chart
# -----------------------------
st.subheader("Sentiment Distribution")

sentiment_chart = (
    filtered_df["Sentiment"]
    .value_counts()
    .reset_index()
)

sentiment_chart.columns = ["Sentiment", "Count"]

fig = px.pie(
    sentiment_chart,
    names="Sentiment",
    values="Count",
    title="Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Company Chart
# -----------------------------
st.subheader("News by Company")

company_chart = (
    filtered_df["Company"]
    .value_counts()
    .reset_index()
)

company_chart.columns = ["Company", "Count"]

fig2 = px.bar(
    company_chart,
    x="Company",
    y="Count",
    title="News Count by Company"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Market Impact Chart
# -----------------------------
st.subheader("Market Impact")

impact_chart = (
    filtered_df["Impact"]
    .value_counts()
    .reset_index()
)

impact_chart.columns = ["Impact", "Count"]

fig3 = px.bar(
    impact_chart,
    x="Impact",
    y="Count",
    title="Market Impact Levels"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Dashboard Loaded Successfully")