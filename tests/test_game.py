import unittest

from game.field import Template, Coordinates, FIELD_TYPES
from game.classic import ClassicGenerator


class TestTemplate(unittest.TestCase):

    def test_Coordinates(self):
        c1 = Coordinates(2, 6)
        c2 = Coordinates(2, 6)
        self.assertTrue(c1 == c2)

    def test_ClassicGenerator(self):
        g = ClassicGenerator()
        self.assertEqual(g.next(Coordinates(0, -1)), 'EXCLUDED')
        self.assertEqual(g.next(Coordinates(0, 0)), 'EXCLUDED')
        self.assertEqual(g.next(Coordinates(0, 1)), 'SEA')
        self.assertEqual(g.next(Coordinates(0, 2)), 'SEA')
        self.assertEqual(g.next(Coordinates(0, 10)), 'SEA')
        self.assertEqual(g.next(Coordinates(0, 11)), 'SEA')
        self.assertEqual(g.next(Coordinates(0, 12)), 'EXCLUDED')
        self.assertEqual(g.next(Coordinates(0, 13)), 'EXCLUDED')

    def test_Template(self):
        t = Template(ClassicGenerator())
        c = Coordinates(4, 12)
        p = t.getPlace(c)
        self.assertEqual(len(t.places), 1)
        c = Coordinates(4, 13)
        p = t.getPlace(c)
        self.assertEqual(len(t.places), 2)
        self.assertEqual(t.getPlace(Coordinates(6, 0)), 'SEA')
        self.assertEqual(t.getPlace(Coordinates(6, 1)), 'GROUND')
