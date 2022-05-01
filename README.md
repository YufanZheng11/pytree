# pytree - A Rich Tree API Implemented in Python

## Progress

| Tree                   | Status             |
|------------------------|--------------------|
| **Binary Tree**        | :fire: In Progress |
| **Binary Search Tree** | :boom: Not Started |
| **N Ary Tree**         | :boom: Not Started |
| **Segment Tree**       | :boom: Not Started |
| **Interval Tree**      | :boom: Not Started |
| **Trie**               | :boom: Not Started |


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
Is Balanced  :  True
Num Leaves   :  4
Is BST       :  False
Is Symmetric :  False
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