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
        value = self.capturedOutput.getvalue()
        value = value.strip().split('\n')[-1]
        self.assertEqual(value, 'key5 3', "Should pass first")
    
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

    def tearDown(self):
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()