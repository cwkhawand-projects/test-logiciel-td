import unittest
from src.exercice_1 import Exercice1


class TestExercice1(unittest.TestCase):
    """Unit tests for Exercice1 methods."""

    def setUp(self):
        self.ex = Exercice1()

    def test_three_biggest_numbers(self):
        """Test the three_biggest_numbers method."""
        self.assertEqual(self.ex.three_biggest_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [9, 6, 5])
        self.assertEqual(self.ex.three_biggest_numbers([10, 20, 30, 40, 50]), [50, 40, 30])
        with self.assertRaises(ValueError):
            self.ex.three_biggest_numbers([1, 2])

    def test_is_prime(self):
        """Test the is_prime method."""
        self.assertTrue(self.ex.is_prime(2))
        self.assertTrue(self.ex.is_prime(3))
        self.assertTrue(self.ex.is_prime(29))
        self.assertFalse(self.ex.is_prime(1))
        self.assertFalse(self.ex.is_prime(4))
        self.assertFalse(self.ex.is_prime(15))

    def test_is_arithmetic_sequence(self):
        """Test the is_arithmetic_sequence method."""
        self.assertTrue(self.ex.is_arithmetic_sequence([2, 4, 6, 8, 10]))
        self.assertTrue(self.ex.is_arithmetic_sequence([5, 10, 15, 20]))
        self.assertFalse(self.ex.is_arithmetic_sequence([1, 2, 4, 7]))
        self.assertFalse(self.ex.is_arithmetic_sequence([10]))


if __name__ == '__main__':
    unittest.main()
