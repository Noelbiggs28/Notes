import unittest
from listfuncs import list_max

class TestListMax(unittest.TestCase):
# defs below must begin with test
    def test_1(self):
        a_list = [6,43,18,100,9,85]
        result = list_max(a_list)
        self.assertEqual(result, 100)

    def test_2(self):
        a_list = [-7,-1,-38,-2,-99]
        result = list_max(a_list)
        self.assertEqual(result, -1)

if __name__== '__main__':
    unittest.main()