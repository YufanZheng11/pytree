import unittest

from tree.BinaryTree import BinaryTree


class TestStringMethods(unittest.TestCase):

    def test_initFromPreorderAndInorder(self):
        tree = BinaryTree.initFromPreorderAndInorder([1, 2, 3, 4, 5, 6, 7], [3, 2, 1, 5, 6, 4, 7])
        tree.pprint()

    def test_initFromInorderAndPostorder(self):
        tree = BinaryTree.initFromInorderAndPostorder([1, 2, 3, 4, 5, 6, 7], [3, 2, 1, 5, 6, 4, 7])
        tree.pprint()


if __name__ == '__main__':
    unittest.main()
