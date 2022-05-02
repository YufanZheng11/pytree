class AvlTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return "<AvlTreeNode val={} height={}>".format(self.val, self.height)
