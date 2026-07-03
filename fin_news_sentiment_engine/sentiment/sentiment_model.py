from transformers import pipeline

class SentimentAnalyzer:

    def __init__(self):
        """
        Load pretrained sentiment analysis model.
        This model is downloaded automatically the first time.
        """

        self.classifier = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest"
        )

    def analyze(self, text):
        """
        Analyze sentiment of a news headline.
        """

        result = self.classifier(text)[0]

        label = result["label"]
        score = round(result["score"], 4)

        # Convert model labels to project labels
        if label.upper() == "POSITIVE":
            sentiment = "Positive"

        elif label.upper() == "NEGATIVE":
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        return {
            "text": text,
            "sentiment": sentiment,
            "confidence": score
        }

    def analyze_multiple(self, headlines):
        """
        Analyze multiple news headlines.
        """

        results = []

        for headline in headlines:
            results.append(self.analyze(headline))

        return results


if __name__ == "__main__":

    analyzer = SentimentAnalyzer()

    sample_news = [
        "Apple reports record quarterly earnings.",
        "Tesla recalls over 50000 vehicles.",
        "Federal Reserve releases monthly report.",
        "Microsoft acquires AI startup.",
        "Amazon revenue remains unchanged."
    ]

    print("=" * 60)
    print("Financial News Sentiment Analysis")
    print("=" * 60)

    for news in sample_news:

        result = analyzer.analyze(news)

        print(f"\nNews       : {result['text']}")
        print(f"Sentiment : {result['sentiment']}")
        print(f"Confidence: {result['confidence']}")