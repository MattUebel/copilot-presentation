import unittest
from presentation.examples.example2 import greet, farewell

class TestExample2(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet(""), "Hello, !")

    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")
        self.assertEqual(farewell("Bob"), "Goodbye, Bob!")
        self.assertEqual(farewell(""), "Goodbye, !")

if __name__ == '__main__':
    unittest.main()
