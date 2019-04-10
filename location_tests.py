import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc2 = Location("Irvine", 36.6, -110)
        self.assertEqual(repr(loc2),"Location('Irvine', 36.6, -110)")

        loc3 = Location("SF", 444.5, 27.7)
        self.assertEqual(repr(loc3),"Location('SF', 444.5, 27.7)")
    

if __name__ == "__main__":
        unittest.main()
