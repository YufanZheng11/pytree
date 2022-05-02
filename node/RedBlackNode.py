# Define Node
class RedBlackTreeNode:
    def __init__(self, val):
        self.val = val  # Value of Node
        self.parent = None  # Parent of Node
        self.left = None  # Left Child of Node
        self.right = None  # Right Child of Node
        self.color = 1  # Red Node as new node is always inserted as Red Node

    def __repr__(self):
        return '<RedBlackTreeNode val={} color={}>'.format(self.val, self.color)
