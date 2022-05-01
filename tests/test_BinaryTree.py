import unittest

from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

TEST_TREE_STR = '\n'.join(line for line in """
  _0_  
 /   \ 
 1   2 
/ \ / \\
3 4 5 6
""".split('\n') if line.strip())


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
        a.left, a.right = b, c
        b.left, b.right = d, e
        c.left, c.right = f, g

        self.tree = BinaryTree(root=a)
        self.subtree = BinaryTree(root=b)

    def test_traversal(self):
        self.assertEqual([node.val for node in self.tree.preorder()], [0, 1, 3, 4, 2, 5, 6])
        self.assertEqual([node.val for node in self.tree.inorder()], [3, 1, 4, 0, 5, 2, 6])
        self.assertEqual([node.val for node in self.tree.postorder()], [3, 4, 1, 5, 6, 2, 0])

    def test_properties(self):
        self.assertEqual(self.tree.getHeight(), 3)
        self.assertEqual(self.tree.getNumberLeaves(), 4)
        self.assertEqual(self.tree.isBalanced(), True)
        self.assertEqual(self.tree.isBinarySearchTree(), False)
        self.assertEqual(self.tree.isSymmetric(), False)

    def test_initFromPreorderAndInorder(self):
        tree = BinaryTree.initFromPreorderAndInorder([0, 1, 3, 4, 2, 5, 6], [3, 1, 4, 0, 5, 2, 6])
        self.assertEqual(tree.pprint(), TEST_TREE_STR)

    def test_initFromInorderAndPostorder(self):
        tree = BinaryTree.initFromInorderAndPostorder([3, 1, 4, 0, 5, 2, 6], [3, 4, 1, 5, 6, 2, 0])
        self.assertEqual(tree.pprint(), TEST_TREE_STR)

    def test_compareTrees(self):
        self.assertEqual(self.tree.isSameTree(self.subtree), False)
        self.assertEqual(self.tree.isSubTreeOf(self.subtree), False)
        self.assertEqual(self.subtree.isSubTreeOf(self.tree), True)

    def test_pathToNode(self):
        a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
        a.left, a.right = b, c
        b.left, b.right = d, e
        c.left, c.right = f, g

        h = BinaryTreeNode(3)
        g.left = h

        tree = BinaryTree(root=a)
        paths = []
        for path in tree.pathToNode(3):
            paths.append('->'.join(str(node.val) for node in path))
        paths.sort()
        self.assertEqual(paths, ['0->1->3', '0->2->6->3'])


if __name__ == '__main__':
    unittest.main()
