import unittest
from car import Level,Car

class ParkingTest(unittest.TestCase):
    def test_level(self):
        level = Level(rows=1, levelNumber =0)
        self.assertTrue(level.park(Car('11')))
        self.assertTrue(level.park(Car('12')))
        self.assertFalse(level.park(Car('13')))
        
if __name__== '__main__':
    unittest.main()
