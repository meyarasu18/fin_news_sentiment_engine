import pandas as pd
import os

class NewsCollector:

    def __init__(self, dataset_path="data/financial_news.csv"):
        """
        Initialize NewsCollector with dataset path.
        """
        self.dataset_path = dataset_path
        self.news_df = None

    def load_news(self):
        """
        Load financial news from CSV.
        """
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        self.news_df = pd.read_csv(self.dataset_path)

        return self.news_df

    def get_all_news(self):
        """
        Return all news records.
        """
        if self.news_df is None:
            self.load_news()

        return self.news_df

    def get_company_news(self, company):
        """
        Return news for a particular company.
        """
        if self.news_df is None:
            self.load_news()

        company_news = self.news_df[
            self.news_df["company"].str.lower() == company.lower()
        ]

        return company_news

    def get_news_by_sentiment(self, sentiment):
        """
        Return news filtered by sentiment.
        """
        if self.news_df is None:
            self.load_news()

        sentiment_news = self.news_df[
            self.news_df["sentiment"].str.lower() == sentiment.lower()
        ]

        return sentiment_news

    def get_latest_news(self, limit=5):
        """
        Return the latest N news articles.
        """
        if self.news_df is None:
            self.load_news()

        latest = self.news_df.sort_values(
            by="date",
            ascending=False
        )

        return latest.head(limit)


if __name__ == "__main__":

    collector = NewsCollector()

    print("=" * 50)
    print("Loading Dataset")
    print("=" * 50)

    news = collector.load_news()

    print(news.head())

    print("\n")

    print("=" * 50)
    print("Tesla News")
    print("=" * 50)

    print(collector.get_company_news("Tesla"))

    print("\n")

    print("=" * 50)
    print("Positive News")
    print("=" * 50)

    print(collector.get_news_by_sentiment("Positive"))

    print("\n")

    print("=" * 50)
    print("Latest 5 News")
    print("=" * 50)

    print(collector.get_latest_news())