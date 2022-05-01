from node.BinaryTreeNode import BinaryTreeNode
from tree.TreeUtils import prettyBinaryTree, initFromPreorderAndInorder, initFromInorderAndPostorder, isBinarySearchTree, isSymmetric
from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin


class BinaryTree(BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin):

    def __init__(self, root):
        if root is not None and not isinstance(root, BinaryTreeNode):
            raise ValueError('Binary tree root must either be None or an instance of BinaryTreeNode')
        self.root = root

    def pprint(self):
        pprintResult = prettyBinaryTree(self.root)
        print(pprintResult)
        return pprintResult

    @staticmethod
    def initFromPreorderAndInorder(preorder, inorder):
        """ Construct a binary tree from preorder and inorder array """
        return BinaryTree(initFromPreorderAndInorder(preorder, inorder))

    @staticmethod
    def initFromInorderAndPostorder(inorder, postorder):
        """ Construct a binary tree from inorder and postorder array """
        return BinaryTree(initFromInorderAndPostorder(inorder, postorder))

    def isBinarySearchTree(self):
        """ Check if a binary tree is a binary search tree """
        return isBinarySearchTree(self.root)

    def isSymmetric(self):
        """ Check if a binary tree is symmetric """
        return isSymmetric(self.root)
