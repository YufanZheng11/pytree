import unittest

from tree.RedBlackTree import RedBlackTree


class TestRedBlackTree(unittest.TestCase):

    def test_insert(self):
        tree = RedBlackTree()
        for i in range(15):
            tree.insert(i)
        tree.pprint()

    def test_delete(self):
        tree = RedBlackTree()
        for i in range(21):
            tree.insert(i)
        tree.delete(15)
        tree.delete(1)
        tree.delete(20)
        tree.pprint()

    def test_search(self):
        tree = RedBlackTree()
        for i in range(21):
            tree.insert(i)
        self.assertIsNotNone(tree.search(10))
        self.assertIsNotNone(tree.search(5))
        self.assertIsNone(tree.search(50))


if __name__ == '__main__':
    unittest.main()
