import unittest
from src.helloworld import HelloWorld


class TestHelloWorld(unittest.TestCase):
    """Unit test for the HelloWorld class."""

    def test_hello_world(self):
        """Test the say_hello method to ensure it returns 'Hello World!'."""
        hello_world_instance = HelloWorld()
        self.assertEqual(hello_world_instance.say_hello(), "Hello World!")


if __name__ == '__main__':
    unittest.main()
