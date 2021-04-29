import unittest
import fullName

class SimpleTest(unittest.TestCase):
    def test_fullName(self):
        self.assertEqual(fullName.full_name("Chelsea", "Li"), "Chelsea Li") 
        self.assertEqual(fullName.full_name ("Chelsea", ""), "Chelsea ")
        self.assertEqual(fullName.full_name ("Chelsea", 1), "Chelsea 1")

if __name__ == '__main__':
	unittest.main()
