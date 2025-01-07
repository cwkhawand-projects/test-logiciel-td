import unittest
from src.exercice_2 import FIFO, LIFO

class TestFIFO(unittest.TestCase):
    """Unit tests for the FIFO class."""

    def setUp(self):
        self.fifo = FIFO()

    def test_enqueue_and_dequeue(self):
        """Test enqueue and dequeue operations."""
        self.fifo.enqueue(1)
        self.fifo.enqueue(2)
        self.fifo.enqueue(3)
        self.assertEqual(self.fifo.dequeue(), 1)
        self.assertEqual(self.fifo.dequeue(), 2)
        self.assertEqual(self.fifo.dequeue(), 3)
        with self.assertRaises(IndexError):
            self.fifo.dequeue()

    def test_is_empty(self):
        """Test the is_empty method."""
        self.assertTrue(self.fifo.is_empty())
        self.fifo.enqueue(10)
        self.assertFalse(self.fifo.is_empty())
        self.fifo.dequeue()
        self.assertTrue(self.fifo.is_empty())

    def test_peek(self):
        """Test the peek method."""
        self.fifo.enqueue(5)
        self.assertEqual(self.fifo.peek(), 5)
        self.fifo.enqueue(10)
        self.assertEqual(self.fifo.peek(), 5)
        self.fifo.dequeue()
        self.assertEqual(self.fifo.peek(), 10)
        self.fifo.dequeue()
        with self.assertRaises(IndexError):
            self.fifo.peek()


class TestLIFO(unittest.TestCase):
    """Unit tests for the LIFO class."""

    def setUp(self):
        self.lifo = LIFO()

    def test_push_and_pop(self):
        """Test push and pop operations."""
        self.lifo.push(1)
        self.lifo.push(2)
        self.lifo.push(3)
        self.assertEqual(self.lifo.pop(), 3)
        self.assertEqual(self.lifo.pop(), 2)
        self.assertEqual(self.lifo.pop(), 1)
        with self.assertRaises(IndexError):
            self.lifo.pop()

    def test_is_empty(self):
        """Test the is_empty method."""
        self.assertTrue(self.lifo.is_empty())
        self.lifo.push(10)
        self.assertFalse(self.lifo.is_empty())
        self.lifo.pop()
        self.assertTrue(self.lifo.is_empty())

    def test_peek(self):
        """Test the peek method."""
        self.lifo.push(5)
        self.assertEqual(self.lifo.peek(), 5)
        self.lifo.push(10)
        self.assertEqual(self.lifo.peek(), 10)
        self.lifo.pop()
        self.assertEqual(self.lifo.peek(), 5)
        self.lifo.pop()
        with self.assertRaises(IndexError):
            self.lifo.peek()


if __name__ == '__main__':
    unittest.main()
