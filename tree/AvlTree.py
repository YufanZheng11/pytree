from node.AvlTreeNode import AvlTreeNode
from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin
from tree.TreeUtils import prettyBinaryTree, isBinarySearchTree, insertAvlVal, deleteAvlVal, initAvlFromSortedArray


class AvlTree(BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin):

    def __init__(self, root=None):
        if root is not None and not isinstance(root, AvlTreeNode):
            raise ValueError('Binary tree root must either be None or an instance of AVLTreeNode')
        if not isBinarySearchTree(root):
            raise ValueError("Root is not a binary search tree")
        self.root = root

    def pprint(self):
        pprintResult = prettyBinaryTree(self.root)
        print(pprintResult)
        return pprintResult

    @staticmethod
    def initFromSortedArray(arr):
        if arr != sorted(arr):
            raise ValueError('Input array is not sorted')
        if len(arr) != len(set(arr)):
            raise ValueError('Input array contains duplicates')
        return AvlTree(initAvlFromSortedArray(arr))

    def insert(self, val):
        self.root = insertAvlVal(self.root, val)

    def delete(self, val):
        self.root = deleteAvlVal(self.root, val)
