import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_basic(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_greet_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
