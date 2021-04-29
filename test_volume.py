import unittest
import volume

class SimpleTest(unittest.TestCase):
    def test_vol(self):
        self.assertEqual(volume.vol(2, 5, 1), 10)
        self.assertEqual(volume.vol(2, '5', 1), 10)
        self.assertEqual(volume.vol(2, -5, 1), 10)

if __name__ == '__main__':
	unittest.main()