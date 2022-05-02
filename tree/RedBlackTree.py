from node.RedBlackNode import RedBlackTreeNode

from tree.TreeMixins import BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin
from tree.TreeUtils import prettyBinaryTree

NULL = RedBlackTreeNode(0)
NULL.color = 0


class RedBlackTree(BinaryTreeTraversalMixin, BinaryTreePropertiesMixin, BinaryTreeCompareMixin, BinaryTreePathMixin):
    def __init__(self):
        self.root = NULL

    # Function to call print
    def pprint(self):
        pprintResult = prettyBinaryTree(self.root)
        print(pprintResult)
        return pprintResult

    # Insert New Node
    def insert(self, val):
        node = RedBlackTreeNode(val)
        node.parent = None
        node.val = val
        node.left = NULL
        node.right = NULL
        node.color = 1  # Set root colour as Red

        y = None
        x = self.root

        while x != NULL:  # Find position for new node
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y  # Set parent of Node as y
        if y is None:  # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < y.val:  # Check if it is right Node or Left Node by checking the value
            y.left = node
        else:
            y.right = node

        if node.parent is None:  # Root node is always Black
            node.color = 0
            return

        if node.parent.parent is None:  # If parent of node is Root Node
            return

        self.__fixInsert(node)  # Else call for Fix Up

    # Deletion of node
    def delete(self, val):
        self.__deleteNodeHelper(self.root, val)  # Call for deletion

    def search(self, val):
        curr = self.root
        while curr != NULL and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr is NULL:
            return
        return curr

    # Code for left rotate
    def __leftRotate(self, x):
        y = x.right  # Y = Right child of x
        x.right = y.left  # Change right child of x to left child of y
        if y.left != NULL:
            y.left.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        if x.parent is None:  # If parent of x == None ie. root node
            self.root = y  # Set y as root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Code for right rotate
    def __rightRotate(self, x):
        y = x.left  # Y = Left child of x
        x.left = y.right  # Change left child of x to right child of y
        if y.right != NULL:
            y.right.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        if x.parent is None:  # If x is root node
            self.root = y  # Set y as root
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix Up Insertion
    def __fixInsert(self, k):
        while k.parent.color == 1:  # While parent is red
            if k.parent == k.parent.parent.right:  # if parent is right child of its parent
                u = k.parent.parent.left  # Left child of grandparent
                if u.color == 1:  # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0  # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # Set grandparent node as Red
                    k = k.parent.parent  # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:  # If k is left child of it's parent
                        k = k.parent
                        self.__rightRotate(k)  # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__leftRotate(k.parent.parent)
            else:  # if parent is left child of its parent
                u = k.parent.parent.right  # Right child of grandparent
                if u.color == 1:  # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0  # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # set color of grandparent as Red
                    k = k.parent.parent  # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:  # if k is right child of its parent
                        k = k.parent
                        self.__leftRotate(k)  # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__rightRotate(k.parent.parent)  # Call right rotate on grandparent
            if k == self.root:  # If k reaches root then break
                break
        self.root.color = 0  # Set color of root as black

    # Function to fix issues after deletion
    def __fixDelete(self, x):
        while x != self.root and x.color == 0:  # Repeat until x reaches nodes and color of x is black
            if x == x.parent.left:  # If x is left child of its parent
                s = x.parent.right  # Sibling of x
                if s.color == 1:  # if sibling is red
                    s.color = 0  # Set its color to black
                    x.parent.color = 1  # Make its parent red
                    self.__leftRotate(x.parent)  # Call for left rotate on parent of x
                    s = x.parent.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1  # Set color of s as red
                    x = x.parent
                else:
                    if s.right.color == 0:  # If right child of s is black
                        s.left.color = 0  # set left child of s as black
                        s.color = 1  # set color of s as red
                        self.__rightRotate(s)  # call right rotation on x
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0  # Set parent of x as black
                    s.right.color = 0
                    self.__leftRotate(x.parent)  # call left rotation on parent of x
                    x = self.root
            else:  # If x is right child of its parent
                s = x.parent.left  # Sibling of x
                if s.color == 1:  # if sibling is red
                    s.color = 0  # Set its color to black
                    x.parent.color = 1  # Make its parent red
                    self.__rightRotate(x.parent)  # Call for right rotate on parent of x
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:  # If left child of s is black
                        s.right.color = 0  # set right child of s as black
                        s.color = 1
                        self.__leftRotate(s)  # call left rotation on x
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.__rightRotate(x.parent)
                    x = self.root
        x.color = 0

    # Function to transplant nodes
    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Function to handle deletion
    def __deleteNodeHelper(self, node, key):
        z = NULL
        while node != NULL:  # Search for the node having that value/ key and store it in 'z'
            if node.val == key:
                z = node

            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == NULL:  # If Kwy is not present then deletion not possible so return
            print("Value not present in Tree !!")
            return

        y = z
        y_original_color = y.color  # Store the color of z- node
        if z.left == NULL:  # If left child of z is NULL
            x = z.right  # Assign right child of z to x
            self.__rb_transplant(z, z.right)  # Transplant Node to be deleted with x
        elif z.right is NULL:  # If right child of z is NULL
            x = z.left  # Assign left child of z to x
            self.__rb_transplant(z, z.left)  # Transplant Node to be deleted with x
        else:  # If z has both the child nodes
            y = self.__minimumValueNode(z.right)  # Find minimum of the right sub tree
            y_original_color = y.color  # Store color of y
            x = y.right
            if y.parent == z:  # If y is child of z
                x.parent = y  # Set parent of x as y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:  # If color is black then fixing is needed
            self.__fixDelete(x)

    def __minimumValueNode(self, node):
        while node.left != NULL:
            node = node.left
        return node