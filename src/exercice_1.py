class Exercice1:
    """A class containing exercice 1 functions."""

    @staticmethod
    def three_biggest_numbers(numbers: list[int]) -> list[int]:
        """
        Return the three largest numbers in a list of integers.

        Args:
            numbers (list[int]): The list of integers.

        Returns:
            list[int]: A list containing the three largest numbers in descending order.
        """
        if len(numbers) < 3:
            raise ValueError("The list must contain at least 3 numbers.")
        return sorted(numbers, reverse=True)[:3]

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Check if a number is prime.

        Args:
            number (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def is_arithmetic_sequence(numbers: list[int]) -> bool:
        """
        Check if a list of numbers represents an arithmetic sequence.

        Args:
            numbers (list[int]): The list of numbers.

        Returns:
            bool: True if the list is an arithmetic sequence, False otherwise.
        """
        if len(numbers) < 2:
            return False
        diff = numbers[1] - numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] - numbers[i - 1] != diff:
                return False
        return True
