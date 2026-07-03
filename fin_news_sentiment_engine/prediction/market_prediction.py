import re


class MarketImpactPredictor:

    def __init__(self):

        # Keywords that usually have strong market impact
        self.high_positive = [
            "record profit",
            "record earnings",
            "acquisition",
            "merger",
            "new contract",
            "partnership",
            "growth",
            "expansion",
            "investment",
            "launch",
            "ai",
            "dividend"
        ]

        self.high_negative = [
            "bankruptcy",
            "fraud",
            "layoffs",
            "recall",
            "investigation",
            "lawsuit",
            "decline",
            "loss",
            "drop",
            "crash",
            "downgrade"
        ]

    def detect_event(self, news):

        news = news.lower()

        for word in self.high_positive:
            if word in news:
                return "Positive Event"

        for word in self.high_negative:
            if word in news:
                return "Negative Event"

        return "General News"

    def predict(self, news, sentiment):

        event = self.detect_event(news)

        impact = "Low"
        prediction = "Stable"

        if sentiment == "Positive":

            if event == "Positive Event":
                impact = "High"
                prediction = "Stock Price Likely to Increase"

            else:
                impact = "Medium"
                prediction = "Slight Increase"

        elif sentiment == "Negative":

            if event == "Negative Event":
                impact = "High"
                prediction = "Stock Price Likely to Decrease"

            else:
                impact = "Medium"
                prediction = "Slight Decrease"

        else:

            impact = "Low"
            prediction = "Market Likely Stable"

        return {
            "news": news,
            "sentiment": sentiment,
            "event": event,
            "impact": impact,
            "prediction": prediction
        }


if __name__ == "__main__":

    predictor = MarketImpactPredictor()

    sample_news = [

        (
            "Apple reports record quarterly earnings.",
            "Positive"
        ),

        (
            "Tesla recalls over 50000 vehicles.",
            "Negative"
        ),

        (
            "Microsoft launches new AI platform.",
            "Positive"
        ),

        (
            "Government releases inflation report.",
            "Neutral"
        )

    ]

    print("=" * 70)
    print("MARKET IMPACT PREDICTION")
    print("=" * 70)

    for news, sentiment in sample_news:

        result = predictor.predict(news, sentiment)

        print("\nNews :", result["news"])
        print("Sentiment :", result["sentiment"])
        print("Detected Event :", result["event"])
        print("Impact :", result["impact"])
        print("Prediction :", result["prediction"])