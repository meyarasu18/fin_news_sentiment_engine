import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (only first time)
nltk.download("punkt")
nltk.download("stopwords")

# Load English stop words
stop_words = set(stopwords.words("english"))


class TextPreprocessor:

    def __init__(self):
        pass

    def clean_text(self, text):
        """
        Clean financial news text.
        """

        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove numbers
        text = re.sub(r"\d+", "", text)

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def tokenize(self, text):
        """
        Convert sentence into words.
        """

        tokens = word_tokenize(text)

        return tokens

    def remove_stopwords(self, tokens):
        """
        Remove common English stop words.
        """

        filtered = [
            word
            for word in tokens
            if word not in stop_words
        ]

        return filtered

    def preprocess(self, text):
        """
        Complete preprocessing pipeline.
        """

        cleaned = self.clean_text(text)

        tokens = self.tokenize(cleaned)

        filtered = self.remove_stopwords(tokens)

        return " ".join(filtered)


if __name__ == "__main__":

    processor = TextPreprocessor()

    sample_news = "Tesla reports record quarterly profits in 2026!!!"

    print("Original News:")
    print(sample_news)

    print()

    cleaned = processor.preprocess(sample_news)

    print("Processed News:")
    print(cleaned)