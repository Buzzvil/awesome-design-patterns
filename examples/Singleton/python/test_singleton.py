from tokenize import Single
from singleton import *
import unittest

class TestSingleton(unittest.TestCase):
  def test_singleton(self):
    c = Coin.instance()
    d = Coin.instance()
    assert c == d
    c.add_coin()
    assert c.get_coin() == 10
    assert d.get_coin() == 10

if __name__ == "__main__":
  unittest.main()