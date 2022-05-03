from tree.TreeUtils import (
    getBinaryTreeHeight, isBinaryTreeBalanced, getNumberLeaves, isSameTree, isSubTreeOf, pathToNode, pathBetweenNodes
)


class BinaryTreeTraversalMixin:

    def preorder(self):
        """ Preorder Visit """
        def preorder(root):
            if root:
                yield root
                yield from preorder(root.left)
                yield from preorder(root.right)

        yield from preorder(self.root)

    def inorder(self):
        """ Inorder Visit """
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root
                yield from inorder(root.right)
        yield from inorder(self.root)

    def postorder(self):
        """ Postorder Visit """
        def postorder(root):
            if root:
                yield from postorder(root.left)
                yield from postorder(root.right)
                yield root
        yield from postorder(self.root)


class BinaryTreePropertiesMixin:
    def getHeight(self):
        """" Get Tree Height """
        return getBinaryTreeHeight(self.root)

    def isBalanced(self):
        """ Check if a binary tree is balanced """
        return isBinaryTreeBalanced(self.root)

    def getNumberLeaves(self):
        """ Get number of leaves of a binary tree """
        return getNumberLeaves(self.root)


class BinaryTreeCompareMixin:
    def isSameTree(self, other):
        """ Check if current tree is same as other """
        return isSameTree(self.root, other.root)

    def isSubTreeOf(self, other):
        """ Check if current tree is subtree of other """
        return isSubTreeOf(self.root, other.root)


class BinaryTreePathMixin:
    def pathToNode(self, nodeOrVal):
        """ Find all paths from root to a node with given node or val """
        yield from pathToNode(self.root, nodeOrVal)

    def pathBetweenNodes(self, nodeA, nodeB):
        """ Find node from node a to b """
        return pathBetweenNodes(self.root, nodeA, nodeB)
