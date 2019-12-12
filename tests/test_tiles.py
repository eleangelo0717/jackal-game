import unittest

import actions.tile
import actions.game

from tiles.tile import Tile
import tiles.pack


class TestTile(unittest.TestCase):
    def test_Tile(self):
        t = Tile()
        result = t.className()
        self.assertEqual(result, 'Tile')
        self.assertFalse(t.isOpened())
        self.assertEqual(t.onOpen(), actions.tile.open)
        self.assertEqual(t.onAction(), actions.game.passageTransition)
        t.open()
        self.assertTrue(t.isOpened())


class TestTilesPack(unittest.TestCase):
    def test_TilesPack(self):
        p = tiles.pack.TilesPack()
        t = Tile()
        self.assertEqual(p.next().className(), t.className())


class TestPack(unittest.TestCase):
    def test_pack_next(self):
        p = tiles.pack.Pack(reuseable=True)
        i = p.next()
        t = Tile()
        result = len(p.items)
        self.assertEqual(result, 1)
        self.assertEqual(i.className(), t.className())
