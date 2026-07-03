import spacy


class EntityExtractor:

    def __init__(self):
        """
        Load spaCy English NLP model.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text):
        """
        Extract named entities from text.
        """

        doc = self.nlp(text)

        entities = []

        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_
            })

        return entities

    def extract_company_names(self, text):
        """
        Extract organization names.
        """

        doc = self.nlp(text)

        companies = []

        for ent in doc.ents:
            if ent.label_ == "ORG":
                companies.append(ent.text)

        return companies

    def extract_money(self, text):
        """
        Extract monetary values.
        """

        doc = self.nlp(text)

        money = []

        for ent in doc.ents:
            if ent.label_ == "MONEY":
                money.append(ent.text)

        return money

    def extract_dates(self, text):
        """
        Extract dates.
        """

        doc = self.nlp(text)

        dates = []

        for ent in doc.ents:
            if ent.label_ == "DATE":
                dates.append(ent.text)

        return dates

    def extract_locations(self, text):
        """
        Extract countries, cities, and geopolitical locations.
        """

        doc = self.nlp(text)

        locations = []

        for ent in doc.ents:
            if ent.label_ in ["GPE", "LOC"]:
                locations.append(ent.text)

        return locations

    def extract_all(self, text):
        """
        Return all extracted information.
        """

        return {
            "companies": self.extract_company_names(text),
            "money": self.extract_money(text),
            "dates": self.extract_dates(text),
            "locations": self.extract_locations(text),
            "entities": self.extract_entities(text)
        }


if __name__ == "__main__":

    extractor = EntityExtractor()

    sample_news = """
    Apple invested $5 billion in India on
    January 15, 2026. CEO Tim Cook announced
    the expansion in New Delhi.
    """

    result = extractor.extract_all(sample_news)

    print("=" * 60)
    print("ENTITY EXTRACTION")
    print("=" * 60)

    print("\nCompanies")
    print(result["companies"])

    print("\nMoney")
    print(result["money"])

    print("\nDates")
    print(result["dates"])

    print("\nLocations")
    print(result["locations"])

    print("\nAll Entities")

    for entity in result["entities"]:
        print(entity)