## Binary Tree API

### Build a binary tree
```python
from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

tree = BinaryTree(root=a)
```

### Pretty print a binary tree
```python
tree.pprint()
```
```
  _0_  
 /   \ 
 1   2 
/ \ / \
3 4 5 6
```

### Traversal a binary tree
- Pre-order
- In-order
- Post-order
```python
for node in tree.preorder():
    print(node.val, end=" ")
for node in tree.inorder():
    print(node.val, end=" ")
for node in tree.postorder():
    print(node.val, end=" ")
```
```
# preorder
0 1 3 4 2 5 6 
# Inorder
3 1 4 0 5 2 6
# Postorder
3 4 1 5 6 2 0 
```

### Check binary tree properties
- Tree height
- Number of leaves
- Is balanced
- Is binary search tree
- is symmetric
```python
print('Tree Height  : ', tree.height())
print('Num Leaves   : ', tree.getNumLeaves())
print('Is Balanced  : ', tree.isBalanced())
print('Is BST       : ', tree.isBinarySearchTree())
print('Is Symmetric : ', tree.isSymmetric())
```
```
Tree Height  :  3
Num Leaves   :  4
Is Balanced  :  True
Is BST       :  False
Is Symmetric :  False
```

### Compare 2 binary trees
- Check if 2 binary trees are same
- Checi if a binary is subtree of other
```python
from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

tree_a = BinaryTree(root=a)
tree_b = BinaryTree(root=b)

print("a and b are same tree? :", tree_a.isSameTree(tree_b))
print("a is subtree of  b?    :", tree_a.isSubTreeOf(tree_b))
print("b is subtree of  a?    :", tree_b.isSubTreeOf(tree_a))
```
```
a and b are same tree? : False
a is subtree of  b?    : False
b is subtree of  a?    : True
```

### Build binary tree from traversal orders
- From preorder & inorder
- From inorder & postorder
```python
tree = BinaryTree.initFromPreorderAndInorder([1, 2, 3], [2, 1, 3])
tree.pprint()

tree = BinaryTree.initFromPreorderAndInorder([1, 2, 3], [2, 1, 3])
tree.pprint()
```

```
# From preorder & inorder
 1 
/ \
2 3

# From inorder & postorder
 _3
/  
1  
 \ 
 2 
```

### Find binary tree path
- Find all paths from root to node
```python
from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

h = BinaryTreeNode(3)
g.left = h

tree = BinaryTree(root=a)

for path in tree.pathToNode(3):
    print('->'.join(str(node.val) for node in path))
```
```
# All path to node with given value 3
0->1->3
0->2->6->3
```