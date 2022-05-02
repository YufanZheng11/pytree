from tree.TreeUtils import (
    preorder, inorder, postorder, getBinaryTreeHeight, isBinaryTreeBalanced, getNumberLeaves, isSameTree, isSubTreeOf,
    pathToNode
)


class BinaryTreeTraversalMixin:

    def preorder(self):
        """ Preorder Visit """
        yield from preorder(self.root)

    def inorder(self):
        """ Inorder Visit """
        yield from inorder(self.root)

    def postorder(self):
        """ Postorder Visit """
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
