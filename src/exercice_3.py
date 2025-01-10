import csv
from collections import defaultdict


class CSVAnalyzer:
    """A class to analyze CSV files and calculate statistics."""

    @staticmethod
    def parse_csv(file_like):
        """
        Parse a CSV file-like object into a list of dictionaries.

        Args:
            file_like: A file-like object containing CSV data.

        Returns:
            list[dict]: A list of rows as dictionaries with keys from the header.
        """
        reader = csv.DictReader(file_like)
        rows = []
        for row in reader:
            row["age"] = int(row["age"])  # Convert age to int
            rows.append(row)
        return rows

    @staticmethod
    def calculate_average_ages(data):
        """
        Calculate the average age for each gender from a list of user data.

        Args:
            data (list[dict]): List of user data where each dict has 'age' and 'gender' keys.

        Returns:
            dict: A dictionary with genders as keys and their average ages as values.
        """
        groups = defaultdict(list)
        for row in data:
            groups[row["gender"]].append(row["age"])
        averages = {
            gender: sum(ages) / len(ages) if ages else 0
            for gender, ages in groups.items()
        }
        return averages

    def analyze_csv(self, file_path):
        """
        Analyze a CSV file to calculate average ages by gender.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            dict: A dictionary with genders as keys and their average ages as values.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            rows = self.parse_csv(file)
        return self.calculate_average_ages(rows)
