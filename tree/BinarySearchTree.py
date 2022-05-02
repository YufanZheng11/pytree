from node.BinaryTreeNode import BinaryTreeNode
from tree.TreeUtils import prettyBinaryTree, isBinarySearchTree, initBstFromSortedArray, insertBstVal, searchBstVal, deleteBstNode
from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin


class BinarySearchTree(BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin):

    def __init__(self, root=None):
        if root is not None and not isinstance(root, BinaryTreeNode):
            raise ValueError('Binary tree root must either be None or an instance of BinaryTreeNode')
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
        return BinarySearchTree(initBstFromSortedArray(arr))

    def insert(self, val):
        """ Insert a val into binary search tree """
        self.root = insertBstVal(self.root, val)

    def search(self, val):
        """ Return node if found, return None if not found """
        return searchBstVal(self.root, val)

    def delete(self, val):
        """ Delete a val into binary search tree """
        self.root = deleteBstNode(self.root, val)
