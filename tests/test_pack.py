import unittest

from pack.main import Pack, listGenerator


class TestPack(unittest.TestCase):
    def test_pack_reuseable(self):
        p = Pack(listGenerator([1, 2]), reuseable=True)
        i = p.next()
        self.assertEqual(len(p.dropped), 1)
        self.assertEqual(i, 1)
        i = p.next()
        self.assertEqual(len(p.dropped), 2)
        self.assertEqual(i, 2)
        i = p.next()
        self.assertEqual(len(p.items), 1)
        self.assertEqual(len(p.dropped), 1)
        self.assertEqual(i, 1)

    def test_pack_unreuseable(self):
        p = Pack(listGenerator([1, 2]))
        i = p.next()
        self.assertEqual(len(p.dropped), 0)
        self.assertEqual(i, 1)
        i = p.next()
        self.assertEqual(len(p.dropped), 0)
        self.assertEqual(i, 2)
        i = p.next()
        self.assertEqual(len(p.items), 0)
        self.assertEqual(len(p.dropped), 0)
        self.assertIsNone(i)
