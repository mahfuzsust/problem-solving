import io
import sys
import unittest
from third import LowestCommonAncestor
from models.node import Node

class TestThird(unittest.TestCase):
    def setUp(self):
        self.lowestCommonAncestor = LowestCommonAncestor()
        self.one = Node(1)
        self.two = Node(2, self.one)
        self.three = Node(3, self.one)
        self.four = Node(4, self.two)
        self.five = Node(5, self.two)
        self.six = Node(6, self.three)
        self.seven = Node(7, self.three)
        self.eight = Node(8, self.four)
        self.nine = Node(9, self.four)

    def test_requirement_1(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.six, self.seven), 3, "Should be three")
    def test_requirement_2(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.three, self.seven), 3, "Should be three")
    def test_leaf(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.eight, self.seven), 1, "Should be one")
    def test_parent_same(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.one, self.seven), 1, "Should be one")
    def test_none(self):
        self.assertEqual(self.lowestCommonAncestor.lca(None, self.nine), None, "Should be none")
    def test_none_2(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.one, None), None, "Should be none")
    def test_string(self):
        self.assertEqual(self.lowestCommonAncestor.lca(self.one, "Hello"), None, "Should be none")
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()