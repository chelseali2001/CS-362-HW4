import unittest
import fullName

class SimpleTest(unittest.TestCase):
    def test_fullName(self):
        self.assertEqual(fullName.full_name("Chelsea", "Li"), "Chelsea Li") 
        
    def test_fullName0(self):
        self.assertEqual(fullName.full_name ("Chelsea", ""), "Chelsea ")
    
    def test_fullName1(self):
        self.assertEqual(fullName.full_name ("Chelsea", 1), "Chelsea 1")

if __name__ == '__main__':
	unittest.main()
