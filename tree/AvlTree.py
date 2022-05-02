from node.AvlTreeNode import AvlTreeNode
from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin
from tree.TreeUtils import prettyBinaryTree, isBinarySearchTree


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

        def initAvlFromSortedArray(arr):
            """ Init an AVLh tree from sorted array """
            if not arr:
                return None
            mid = (len(arr)) / 2
            root = AvlTreeNode(arr[mid])
            root.left = initAvlFromSortedArray(arr[:mid])
            root.right = initAvlFromSortedArray(arr[mid + 1:])
            return root

        return AvlTree(initAvlFromSortedArray(arr))

    def insert(self, val):

        def insertAvlVal(root, val):
            """ Insert a value to AVL Tree """
            if root is None:
                return AvlTreeNode(val)
            elif val <= root.val:
                root.left = insertAvlVal(root.left, val)
            elif val > root.val:
                root.right = insertAvlVal(root.right, val)
            root.height = 1 + max(self._avlHeight(root.left), self._avlHeight(root.right))
            balance = self._avlBalance(root)
            if balance > 1 and root.left.val > val:
                return self._avlRotateRight(root)
            if balance < -1 and val > root.right.val:
                return self._avlRotateLeft(root)
            if balance > 1 and val > root.left.val:
                root.left = self._avlRotateLeft(root.left)
                return self._avlRotateRight(root)
            if balance < -1 and val < root.right.val:
                root.right = self._avlRotateRight(root.right)
                return self._avlRotateLeft(root)
            return root

        self.root = insertAvlVal(self.root, val)

    def delete(self, val):

        def deleteAvlVal(node, val):
            """ Delete a value from AVL Tree """
            if node is None:
                return node
            elif val < node.val:
                node.left = deleteAvlVal(node.left, val)
            elif val > node.val:
                node.right = deleteAvlVal(node.right, val)
            else:
                if node.left is None:
                    lt = node.right
                    return lt
                elif node.right is None:
                    lt = node.left
                    return lt
                rgt = self._minAvlValueNode(node.right)
                node.val = rgt.val
                node.right = deleteAvlVal(node.right, rgt.val)
            if node is None:
                return node
            node.height = 1 + max(self._avlHeight(node.left), self._avlHeight(node.right))
            balance = self._avlBalance(node)
            if balance > 1 and self._avlBalance(node.left) >= 0:
                return self._avlRotateRight(node)
            if balance < -1 and self._avlBalance(node.right) <= 0:
                return self._avlRotateLeft(node)
            if balance > 1 and self._avlBalance(node.left) < 0:
                node.left = self._avlRotateLeft(node.left)
                return self._avlRotateRight(node)
            if balance < -1 and self._avlBalance(node.right) > 0:
                node.right = self._avlRotateRight(node.right)
                return self._avlRotateLeft(node)
            return node

        self.root = deleteAvlVal(self.root, val)

    def search(self, val):

        def searchAvlVal(root, val):
            """ A utility function to search a given val in AVL Tree """
            if root is None or root.val == val:
                return root
            if root.val < val:
                return searchAvlVal(root.right, val)
            return searchAvlVal(root.left, val)

        return searchAvlVal(self.root, val)

    def _avlHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def _avlBalance(self, node):
        if node is None:
            return 0
        else:
            return self._avlHeight(node.left) - self._avlHeight(node.right)

    def _minAvlValueNode(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self._minAvlValueNode(node.left)

    def _avlRotateRight(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self._avlHeight(node.left), self._avlHeight(node.right))
        a.height = 1 + max(self._avlHeight(a.left), self._avlHeight(a.right))
        return a

    def _avlRotateLeft(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self._avlHeight(node.left), self._avlHeight(node.right))
        a.height = 1 + max(self._avlHeight(a.left), self._avlHeight(a.right))
        return a