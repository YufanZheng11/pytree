import unittest

from tree.AVLTree import AVLTree


class TestBinaryTree(unittest.TestCase):

    def test_insert(self):
        tree = AVLTree()
        for i in range(15):
            tree.insert(i)
        tree.pprint()

    def test_delete(self):
        tree = AVLTree()
        for i in range(21):
            tree.insert(i)
        tree.delete(15)
        tree.delete(1)
        tree.delete(20)
        tree.pprint()
