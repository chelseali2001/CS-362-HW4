import unittest
import average

class SimpleTest(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average.avg([2, 5, 2]), 3.0) 
    
    def test_average0(self):
        self.assertEqual(average.avg([]), 0.0)
    
    def test_average1(self):
        self.assertEqual(average.avg([0, 0, 0]), 0.0)

if __name__ == '__main__':
	unittest.main()
