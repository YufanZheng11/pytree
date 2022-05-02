import unittest

from tree.AvlTree import AvlTree


class TestAvlTree(unittest.TestCase):

    def test_insert(self):
        tree = AvlTree()
        for i in range(15):
            tree.insert(i)
        tree.pprint()

    def test_delete(self):
        tree = AvlTree()
        for i in range(21):
            tree.insert(i)
        tree.delete(15)
        tree.delete(1)
        tree.delete(20)
        tree.pprint()
