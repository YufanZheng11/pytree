from node.BinaryTreeNode import BinaryTreeNode
from tree.TreeUtils import prettyBinaryTree, isBinarySearchTree
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

        def initBstFromSortedArray(arr):
            """ Init a binary search tree from sorted array """
            if not arr:
                return None
            mid = (len(arr)) / 2
            root = BinaryTreeNode(arr[mid])
            root.left = initBstFromSortedArray(arr[:mid])
            root.right = initBstFromSortedArray(arr[mid + 1:])
            return root

        return BinarySearchTree(initBstFromSortedArray(arr))

    def insert(self, val):
        """ Insert a val into binary search tree """

        def insertBstVal(root, val):
            """ Insert value to binary search tree """
            if root is None:
                return BinaryTreeNode(val)
            else:
                if root.val == val:
                    return root
                elif root.val < val:
                    root.right = insertBstVal(root.right, val)
                else:
                    root.left = insertBstVal(root.left, val)
            return root

        self.root = insertBstVal(self.root, val)

    def search(self, val):
        """ Return node if found, return None if not found """

        def searchBstVal(root, val):
            """ A utility function to search a given val in BST """
            if root is None or root.val == val:
                return root
            if root.val < val:
                return searchBstVal(root.right, val)
            return searchBstVal(root.left, val)

        return searchBstVal(self.root, val)

    def delete(self, val):
        """ Delete a val into binary search tree """

        def deleteBstVal(root, val):
            """ Delete a node from binary search tree """
            if root is None:
                return root
            if val < root.val:
                root.left = deleteBstVal(root.left, val)
            elif val > root.val:
                root.right = deleteBstVal(root.right, val)
            else:
                if root.left is None:
                    temp = root.right
                    return temp
                elif root.right is None:
                    temp = root.left
                    return temp
                temp = _minBstValueNode(root.right)
                root.val = temp.val
                root.right = deleteBstVal(root.right, temp.val)
            return root

        def _minBstValueNode(node):
            """ Find min value node from binary search tree """
            current = node
            while current.left is not None:
                current = current.left
            return current

        self.root = deleteBstVal(self.root, val)
