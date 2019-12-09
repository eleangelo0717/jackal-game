import unittest

from declaration import *

class Test_getField(unittest.TestCase):

    def test_main(self):
        self.assertEqual(getField('from')['key'], 'date_from')
        self.assertEqual(getField('to')['key'], 'date_to')
        self.assertEqual(getField('name')['text'], 'Име')
    
