import unittest

from pack.pack import Pack


class TestPack(unittest.TestCase):
    def test_pack_reuseable(self):
        p = Pack(reuseable=True)
        i = p.next()
        result = len(p.items)
        self.assertEqual(result, 1)
        self.assertEqual(i0, 0)