import unittest

import src
from src.common_shortest_node import get_common_node

class TestSecond(unittest.TestCase):
    def setUp(self):
        self.edges = [
            ("A", "C", 5),
            ("A", "E", 3),
            ("A", "I", 1),
            ("C", "D", 8),
            ("C", "E", 6),
            ("E", "B", 9),
            ("E", "G", 5),
            ("I", "G", 2),
            ("D", "B", 5),
            ("G", "H", 3),
            ("H", "B", 8)
        ]
    
    def test_with_valid_input(self): 
        self.assertEqual(get_common_node(self.edges, 'A', 'B'), 'E', "Should be in center")
    
    def test_with_undirected_input(self): 
        self.assertEqual(get_common_node(self.edges, 'I', 'B'), 'E', "Should be in center")
    
    def test_empty_edge_array(self):
        self.assertIsNone(get_common_node([], "I", "A"), "Should be empty")

    def test_all_none(self):
        self.assertIsNone(get_common_node(None, None, None), "Should be empty")
    
    def test_dest_none(self):
        self.assertIsNone(get_common_node(self.edges, "A", None), "Should be empty")
    
    def test_source_none(self):
        self.assertIsNone(get_common_node(self.edges, None, "A"), "Should be empty")
    
    def test_dest_array(self):
        self.assertIsNone(get_common_node(self.edges, "A", []), "Should be empty")
    
    def test_source_array(self):
        self.assertIsNone(get_common_node(self.edges, [], "A"), "Should be empty")

    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()