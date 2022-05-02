from node.AVLTreeNode import AVLTreeNode
from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin
from tree.TreeUtils import prettyBinaryTree, isBinarySearchTree, insertAvlVal, deleteAvlVal


class AVLTree(BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin):

    def __init__(self, root=None):
        if root is not None and not isinstance(root, AVLTreeNode):
            raise ValueError('Binary tree root must either be None or an instance of AVLTreeNode')
        if not isBinarySearchTree(root):
            raise ValueError("Root is not a binary search tree")
        self.root = root

    def pprint(self):
        pprintResult = prettyBinaryTree(self.root)
        print(pprintResult)
        return pprintResult

    def insert(self, val):
        self.root = insertAvlVal(self.root, val)

    def delete(self, val):
        self.root = deleteAvlVal(self.root, val)
