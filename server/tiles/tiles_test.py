import unittest

from tiles import TileCardChest

class TestTileCardChest(unittest.TestCase):
    def test_TileCardChest_money(self):
        t = TileCardChest(2)
        result = t.money
        self.assertEqual(result, 2)



