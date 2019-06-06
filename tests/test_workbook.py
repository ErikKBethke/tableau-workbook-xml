from unittest import TestCase

import tableauxml

class Workbook(TestCase):
    def test_is_string(self):
        s = tableauxml.test()
        self.assertTrue(isinstance(s, basestring))
