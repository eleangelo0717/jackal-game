import unittest

from pack.pack import Pack


class TestPack(unittest.TestCase):
    def test_pack_next(self):
        data = [1, 2, 3]
        p = Pack(data)
        _ = p.Next()
        result = len(p.items)
        self.assertEqual(result, 2)

    def test_pack_next_last(self):
        data = [1]
        p = Pack(data)
        _ = p.Next()
        result = len(p.items)
        self.assertEqual(result, 0)

    def test_pack_next_empty(self):
        data = []
        p = Pack(data)
        result = p.Next()
        self.assertEqual(result, None)
