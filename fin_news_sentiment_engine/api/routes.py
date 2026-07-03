from flask import Blueprint, jsonify

from news.news_collector import NewsCollector
from sentiment.sentiment_model import SentimentAnalyzer
from prediction.market_prediction import MarketImpactPredictor

# Create Blueprint
api = Blueprint("api", __name__)

# Initialize modules
collector = NewsCollector()
analyzer = SentimentAnalyzer()
predictor = MarketImpactPredictor()


@api.route("/news", methods=["GET"])
def get_news():
    """
    Return all news.
    """
    df = collector.load_news()

    return jsonify(df.to_dict(orient="records"))


@api.route("/sentiment", methods=["GET"])
def get_sentiment():

    df = collector.load_news()

    results = []

    for _, row in df.iterrows():

        sentiment = analyzer.analyze(row["headline"])

        results.append({
            "company": row["company"],
            "headline": row["headline"],
            "sentiment": sentiment["sentiment"],
            "confidence": sentiment["confidence"]
        })

    return jsonify(results)


@api.route("/prediction", methods=["GET"])
def get_prediction():

    df = collector.load_news()

    results = []

    for _, row in df.iterrows():

        sentiment = analyzer.analyze(row["headline"])

        prediction = predictor.predict(
            row["headline"],
            sentiment["sentiment"]
        )

        results.append({
            "company": row["company"],
            "headline": row["headline"],
            "sentiment": sentiment["sentiment"],
            "impact": prediction["impact"],
            "prediction": prediction["prediction"]
        })

    return jsonify(results)


@api.route("/company/<company>", methods=["GET"])
def company_news(company):

    df = collector.get_company_news(company)

    if df.empty:
        return jsonify({
            "message": "Company not found."
        }), 404

    results = []

    for _, row in df.iterrows():

        sentiment = analyzer.analyze(row["headline"])

        prediction = predictor.predict(
            row["headline"],
            sentiment["sentiment"]
        )

        results.append({
            "company": row["company"],
            "headline": row["headline"],
            "sector": row["sector"],
            "sentiment": sentiment["sentiment"],
            "confidence": sentiment["confidence"],
            "impact": prediction["impact"],
            "prediction": prediction["prediction"]
        })

    return jsonify(results)


@api.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "Running",
        "project": "AI-Powered Financial News & Sentiment Analysis Engine"
    })