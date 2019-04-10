import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests max_list_iter"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([20,30,40,60,60]),60)
        self.assertEqual(max_list_iter([100,30,40,60,60]),100)
        self.assertEqual(max_list_iter([20,30,500,60,60]),500)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([2,6]),[6,2])
        self.assertEqual(reverse_rec([2,2,3,3]),[3,3,2,2])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5)
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)

        list_2 = [20,21,24,28,28,29]
        self.assertEqual(bin_search(24, 0, len(list_2)-1, list_2), 2)
        


if __name__ == "__main__":
        unittest.main()

    
