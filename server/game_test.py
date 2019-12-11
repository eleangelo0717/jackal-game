import unittest

from game import Game
from tiles import TileCardChest, TileCardTreasure, TileCardRum

class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_items(self):
        items = self.g.items
        self.assertEqual(len(self.g.items), 67)
        self.assertEqual(len([item for item in items if item.className() == 'Ship']), 4)
        self.assertEqual(len([item for item in items if item.className() == 'Pirate']), 12)
        self.assertEqual(len([item for item in items if item.className() == 'Missionary']), 1)
        self.assertEqual(len([item for item in items if item.className() == 'Friday']), 1)
        self.assertEqual(len([item for item in items if item.className() == 'BenGunn']), 1)
        self.assertEqual(len([item for item in items if item.className() == 'Coin']), 37)
        self.assertEqual(len([item for item in items if item.className() == 'Treasure']), 1)
        self.assertEqual(len([item for item in items if item.className() == 'Bottle']), 10)

        item = self.g.getFreeItem('Ship')
        self.assertIsNone(item)

        item = self.g.getFreeItem('Pirate')
        self.assertIsNone(item)

        item = self.g.getFreeItem('Missionary')
        self.assertIsNotNone(item)

        item = self.g.getFreeItem('Friday')
        self.assertIsNotNone(item)

        item = self.g.getFreeItem('BenGunn')
        self.assertIsNotNone(item)

        item = self.g.getFreeItem('Coin')
        self.assertIsNotNone(item)

        item = self.g.getFreeItem('Treasure')
        self.assertIsNotNone(item)

        item = self.g.getFreeItem('Bottle')
        self.assertIsNotNone(item)


    def test_gamers(self):
        self.assertEqual(len(self.g.gamers), 4)


    def test_field(self):
        field = self.g.field
        self.assertEqual(field.game, self.g)
        p = field.getPlaceByCoordinates(0,0)
        self.assertIsNone(p)
        p = field.getPlaceByCoordinates(6,6)
        self.assertIsNotNone(p)


    def test_TileCardChest(self):
        tile = TileCardChest(3)
        items = self.g.items
        p = self.g.field.getPlaceByCoordinates(6,6)
        c = [item for item in items if item.className() == 'Pirate'][0]
        p.placeTile(tile)
        p.tile.activate(c)
        self.assertEqual(len([item for item in items if item.className() == 'Coin' and item.x is None]), 34)
        self.assertEqual(len([item for item in p.getItems() if item.className() == 'Coin']), 3)


    def test_TileCardTreasure(self):
        tile = TileCardTreasure()
        items = self.g.items
        p = self.g.field.getPlaceByCoordinates(6,6)
        c = [item for item in items if item.className() == 'Pirate'][0]
        p.placeTile(tile)
        p.tile.activate(c)
        self.assertEqual(len([item for item in items if item.className() == 'Treasure' and item.x is None]), 0)
        self.assertEqual(len([item for item in p.getItems() if item.className() == 'Treasure']), 1)


    def test_TileCardRum(self):
        tile = TileCardRum(3)
        items = self.g.items
        p = self.g.field.getPlaceByCoordinates(6,6)
        c = [item for item in items if item.className() == 'Pirate'][0]
        p.placeTile(tile)
        p.tile.activate(c)
        self.assertEqual(len([item for item in items if item.className() == 'Bottle' and item.x is None]), 7)
        ship = c.gamer.getShip()
        self.assertEqual(len([item for item in ship.getItems() if item.className() == 'Bottle']), 3)

