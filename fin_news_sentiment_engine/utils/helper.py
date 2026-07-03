import os
from datetime import datetime
import pandas as pd


class Helper:

    @staticmethod
    def create_output_folder():
        """
        Create outputs folder if it doesn't exist.
        """
        os.makedirs("outputs", exist_ok=True)

    @staticmethod
    def current_time():
        """
        Return current date and time.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def confidence_percentage(score):
        """
        Convert confidence score into percentage.
        Example:
        0.9876 -> 98.76%
        """
        return round(score * 100, 2)

    @staticmethod
    def save_csv(dataframe, filename):
        """
        Save DataFrame to CSV.
        """
        Helper.create_output_folder()

        path = os.path.join("outputs", filename)

        dataframe.to_csv(path, index=False)

        print(f"Report saved to: {path}")

    @staticmethod
    def load_csv(path):
        """
        Load CSV file.
        """
        return pd.read_csv(path)

    @staticmethod
    def print_title(title):
        """
        Print formatted title.
        """
        print("=" * 60)
        print(title)
        print("=" * 60)

    @staticmethod
    def print_news(result):
        """
        Print formatted news analysis.
        """

        print("-" * 60)
        print(f"Company      : {result['company']}")
        print(f"Headline     : {result['headline']}")
        print(f"Sentiment    : {result['sentiment']}")
        print(f"Confidence   : {result['confidence']}%")
        print(f"Impact       : {result['impact']}")
        print(f"Prediction   : {result['prediction']}")
        print("-" * 60)