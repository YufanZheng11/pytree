class BinaryTreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "<BinaryTreeNode val={}>".format(self.val)
