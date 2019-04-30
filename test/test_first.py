import io
import sys
import unittest

import src
from src.first import print_depth

class TestFirst(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def test_basic(self): 
        print_depth({'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4}}})
        self.assertEqual(self.capturedOutput.getvalue(), 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n', "Should pass basic")
    
    def test_empty_dictionary(self):
        print_depth({})
        self.assertEqual(self.capturedOutput.getvalue(), '', "Should be empty")
    
    def test_None(self):
        print_depth(None)
        self.assertEqual(self.capturedOutput.getvalue(), '', "Should be empty")
    
    def test_Array(self):
        print_depth([])
        self.assertEqual(self.capturedOutput.getvalue(), '', "Should be empty")
    
    def test_String(self):
        print_depth("Hello world")
        self.assertEqual(self.capturedOutput.getvalue(), '', "Should be empty")

    def test_basic(self): 
        print_depth({'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4}}, 'key6': 6})
        self.assertEqual(self.capturedOutput.getvalue(), 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nkey6 1\n', "Should pass basic")
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()