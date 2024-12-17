import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
import src.helloworld as hw

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        HelloWorld = hw.HelloWorld()
        self.assertEqual(HelloWorld.say_hello(), "Hello World!")

if __name__ == '__main__':
    unittest.main()