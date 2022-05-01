from tree.TreeUtils import getBinaryTreeHeight, isBinaryTreeBalanced, getNumLeaves, isSameTree, isSubTreeOf


class BinaryTreeTraversalMixin:

    def preorder(self):
        """ Preorder Visit """
        def preorderHelper(root):
            if root:
                yield root
                yield from preorderHelper(root.left)
                yield from preorderHelper(root.right)
        yield from preorderHelper(self.root)

    def inorder(self):
        """ Inorder Visit """
        def inorderHelper(root):
            if root:
                yield from inorderHelper(root.left)
                yield root
                yield from inorderHelper(root.right)
        yield from inorderHelper(self.root)

    def postorder(self):
        """ Postorder Visit """
        def postorderHelper(root):
            if root:
                yield from postorderHelper(root.left)
                yield from postorderHelper(root.right)
                yield root
        yield from postorderHelper(self.root)


class BinaryTreePropertiesMixin:
    def height(self):
        """" Get Tree Height """
        return getBinaryTreeHeight(self.root)

    def isBalanced(self):
        """ Check if a binary tree is balanced """
        return isBinaryTreeBalanced(self.root)

    def getNumLeaves(self):
        """ Get number of leaves of a binary tree """
        return getNumLeaves(self.root)


class BinaryTreeCompareMixin:
    def isSameTree(self, other):
        """ Check if current tree is same as other """
        return isSameTree(self.root, other.root)

    def isSubTreeOf(self, other):
        """ Check if current tree is subtree of other """
        return isSubTreeOf(self.root, other.root)
