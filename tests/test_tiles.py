import unittest

import actions.tile
import actions.game

from tiles.tile import Tile


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
