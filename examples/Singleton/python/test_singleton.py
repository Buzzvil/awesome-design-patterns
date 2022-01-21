from singleton import *
import unittest


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        c = Logger()
        d = Logger()
        assert c is d


if __name__ == "__main__":
    unittest.main()
