import unittest
from io import StringIO
from src.exercice_3 import CSVAnalyzer


class TestCSVAnalyzer(unittest.TestCase):
    """Unit tests for the CSVAnalyzer class."""

    def setUp(self):
        self.analyzer = CSVAnalyzer()
        self.csv_data = StringIO(
            "name,age,gender\n"
            "Alice,25,female\n"
            "Bob,30,male\n"
            "Carol,40,female\n"
            "David,35,male\n"
        )

    def test_parse_csv(self):
        """Test the parse_csv method."""
        rows = self.analyzer.parse_csv(self.csv_data)
        expected = [
            {"name": "Alice", "age": 25, "gender": "female"},
            {"name": "Bob", "age": 30, "gender": "male"},
            {"name": "Carol", "age": 40, "gender": "female"},
            {"name": "David", "age": 35, "gender": "male"},
        ]
        self.assertEqual(rows, expected)

    def test_calculate_average_ages(self):
        """Test the calculate_average_ages method."""
        data = [
            {"name": "Alice", "age": 25, "gender": "female"},
            {"name": "Bob", "age": 30, "gender": "male"},
            {"name": "Carol", "age": 40, "gender": "female"},
            {"name": "David", "age": 35, "gender": "male"},
        ]
        averages = self.analyzer.calculate_average_ages(data)
        self.assertEqual(averages, {"male": 32.5, "female": 32.5})

    def test_calculate_average_ages_empty(self):
        """Test calculate_average_ages with empty data."""
        self.assertEqual(self.analyzer.calculate_average_ages([]), {})

    def test_analyze_csv(self):
        """Test the analyze_csv method."""
        # Mock a file path by writing to a temporary file-like object
        with open("test_users.csv", "w", encoding="utf-8") as f:
            f.write(
                "name,age,gender\n"
                "Alice,25,female\n"
                "Bob,30,male\n"
                "Carol,40,female\n"
                "David,35,male\n"
            )
        result = self.analyzer.analyze_csv("test_users.csv")
        self.assertEqual(result, {"male": 32.5, "female": 32.5})

if __name__ == "__main__":
    unittest.main()
