import unittest

import src
from src.sorted_list_max import get_largest_item

class TestSecond(unittest.TestCase):
    def setUp(self):
        self.arr = [5, 6, 7, 9, 11, 345, 567, 1, 3]
    
    def test_with_random_order(self):
        self.assertEqual(get_largest_item(self.arr), 567, "Find the largest number")
    
    def test_with_sorted_array(self):
        self.assertEqual(get_largest_item(self.arr[:-2]), 567, "Find the largest number in sorted")
    
    def test_None(self):
        self.assertIsNone(get_largest_item(None), "Should be empty")
    
    def test_Array(self):
        self.assertIsNone(get_largest_item([]), "Should be empty")
    
    def test_String(self):
        self.assertIsNone(get_largest_item("Hello world"), "Should be empty")

    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()