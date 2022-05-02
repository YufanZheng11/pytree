from collections import Counter

from node.BinaryTreeNode import BinaryTreeNode


# --------------------------------------------------------------------------------------------------------------
# Binary Tree Traversal
# --------------------------------------------------------------------------------------------------------------

def preorder(root):
    if root:
        yield root
        yield from preorder(root.left)
        yield from preorder(root.right)


def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root
        yield from inorder(root.right)


def postorder(root):
    if root:
        yield from postorder(root.left)
        yield from postorder(root.right)
        yield root


# --------------------------------------------------------------------------------------------------------------
# Build Binary Tree Utils
# --------------------------------------------------------------------------------------------------------------

def initFromPreorderAndInorder(preorder, inorder):
    """ Construct a binary tree from preorder and inorder array """
    _validateTraversalInputs(preorder, inorder)

    def buildHelper(preorder, inorder):
        if not preorder:
            return None
        rootVal = preorder[0]
        index = inorder.index(rootVal)
        root = BinaryTreeNode(rootVal)
        root.left = buildHelper(preorder[1:index + 1], inorder[:index])
        root.right = buildHelper(preorder[index + 1:], inorder[index + 1:])
        return root

    return buildHelper(preorder, inorder)


def initFromInorderAndPostorder(inorder, postorder):
    """ Construct a binary tree from preorder and inorder array """
    _validateTraversalInputs(inorder, postorder)

    def buildHelper(inorder, postorder):
        if not inorder:
            return None
        rootVal = postorder[-1]
        index = inorder.index(rootVal)
        root = BinaryTreeNode(rootVal)
        root.left = buildHelper(inorder[:index], postorder[:index])
        root.right = buildHelper(inorder[index + 1:], postorder[index:-1])
        return root

    return buildHelper(inorder, postorder)


def _validateTraversalInputs(order1, order2):
    if not isinstance(order1, (list, tuple)) or not isinstance(order2, (list, tuple)):
        raise ValueError('Inputs must be either list or tuple')
    if len(order1) != len(order2):
        raise ValueError('Inputs have different size')
    count1 = Counter(order1)
    count2 = Counter(order2)
    if count1 != count2:
        raise ValueError('Inputs have different values')
    if any(count > 1 for count in count1.values()):
        raise ValueError('Inputs must not contain duplicate values')


# --------------------------------------------------------------------------------------------------------------
#  Binary Tree Metrics
# --------------------------------------------------------------------------------------------------------------

def getBinaryTreeHeight(root):
    """ Get height of a binary tree """
    if root is None:
        return 0
    return max(getBinaryTreeHeight(root.left), getBinaryTreeHeight(root.right)) + 1


def isBinaryTreeBalanced(root):
    """ Check if a binary tree is balanced """
    if root is None:
        return True
    lh = getBinaryTreeHeight(root.left)
    rh = getBinaryTreeHeight(root.right)
    if (abs(lh - rh) <= 1) and isBinaryTreeBalanced(root.left) is True and isBinaryTreeBalanced(root.right) is True:
        return True
    return False


def getNumberLeaves(root):
    """ Get number of leaves """
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return getNumberLeaves(root.left) + getNumberLeaves(root.right)


def isBinarySearchTree(root):
    def isBstHelper(root, low, high):
        if root is None:
            return True
        if root.val < low or root.val > high:
            return False
        return (isBstHelper(root.left, low, root.val - 1) and
                isBstHelper(root.right, root.val + 1, high))

    return isBstHelper(root, float('-inf'), float('inf'))


def isSymmetric(root):
    def isMirror(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return (isMirror(root1.left, root2.right) and
                        isMirror(root1.right, root2.left))
        return False

    return isMirror(root, root)


# --------------------------------------------------------------------------------------------------------------
#  Binary Tree Compare
# --------------------------------------------------------------------------------------------------------------

def isSameTree(a, b):
    """ Check if 2 trees are same or not """
    # 1. Both empty
    if a is None and b is None:
        return True

    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.val == b.val) and
                isSameTree(a.left, b.left) and
                isSameTree(a.right, b.right))

    # 3. one empty, one not -- false
    return False


def isSubTreeOf(subtree, tree):
    """ Function to check if a given binary tree is a subtree of another binary tree or not """
    # base case: both trees are the same
    if tree == subtree:
        return True

    # base case: if the first tree is empty but the second tree is non-empty
    if tree is None:
        return False

    # store the inorder traversal of both trees in `first` and `second`, respectively
    first = list(inorder(tree))
    second = list(inorder(subtree))

    def isSubList(x, y):
        for i in range(len(x) - len(y) + 1):
            if x[i:i+len(y)] == y:
                return True
        return False

    # return false if the second list is not a sublist of the first list
    if not isSubList(first, second):
        return False

    # Now store postorder traversal of both trees in `first` and `second`, respectively
    first = list(postorder(tree))
    second = list(postorder(subtree))

    # return false if the second list is not a sublist of the first list
    if not isSubList(first, second):
        return False

    return True


# --------------------------------------------------------------------------------------------------------------
#  Binary Tree Path Utils
# --------------------------------------------------------------------------------------------------------------

def pathToNode(root, nodeOrVal):
    if root:
        if root == nodeOrVal or root.val == nodeOrVal:
            yield [root]
        for path in pathToNode(root.left, nodeOrVal):
            yield [root] + path
        for path in pathToNode(root.right, nodeOrVal):
            yield [root] + path


# --------------------------------------------------------------------------------------------------------------
#  Binary Tree Pretty Formatter
# --------------------------------------------------------------------------------------------------------------

def prettyBinaryTree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    return '\n'.join(lines)
