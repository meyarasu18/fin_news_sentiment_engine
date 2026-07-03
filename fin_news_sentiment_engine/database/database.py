import sqlite3


class DatabaseManager:

    def __init__(self, db_name="database/financial_news.db"):
        """
        Initialize SQLite database.
        """
        self.db_name = db_name
        self.create_table()

    def connect(self):
        """
        Create database connection.
        """
        return sqlite3.connect(self.db_name)

    def create_table(self):
        """
        Create news_analysis table.
        """
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            sector TEXT,

            headline TEXT,

            sentiment TEXT,

            confidence REAL,

            impact TEXT,

            prediction TEXT
        )
        """)

        conn.commit()
        conn.close()

    def insert_news(self,
                    company,
                    sector,
                    headline,
                    sentiment,
                    confidence,
                    impact,
                    prediction):
        """
        Insert one analyzed news record.
        """

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO news_analysis
        (
            company,
            sector,
            headline,
            sentiment,
            confidence,
            impact,
            prediction
        )

        VALUES
        (?, ?, ?, ?, ?, ?, ?)

        """,
        (
            company,
            sector,
            headline,
            sentiment,
            confidence,
            impact,
            prediction
        ))

        conn.commit()
        conn.close()

    def fetch_all(self):
        """
        Return all records.
        """

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM news_analysis")

        rows = cursor.fetchall()

        conn.close()

        return rows

    def fetch_company(self, company):
        """
        Return records of one company.
        """

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM news_analysis WHERE company=?",
            (company,)
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    def delete_all(self):
        """
        Delete every record.
        """

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM news_analysis")

        conn.commit()
        conn.close()


if __name__ == "__main__":

    db = DatabaseManager()

    db.delete_all()

    db.insert_news(
        company="Tesla",
        sector="Automobile",
        headline="Tesla reports record quarterly earnings",
        sentiment="Positive",
        confidence=0.98,
        impact="High",
        prediction="Stock Price Likely to Increase"
    )

    db.insert_news(
        company="Apple",
        sector="Technology",
        headline="Apple launches new AI service",
        sentiment="Positive",
        confidence=0.96,
        impact="High",
        prediction="Stock Price Likely to Increase"
    )

    print("=" * 60)
    print("DATABASE RECORDS")
    print("=" * 60)

    records = db.fetch_all()

    for record in records:
        print(record)