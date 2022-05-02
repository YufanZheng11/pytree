# pytree - A Rich Tree API Implemented in Python

## Progress

| Tree                                  | Status             |
|---------------------------------------|--------------------|
| [**Binary Tree**](docs/BinaryTree.md) | :white_check_mark: Completed   |
| **Binary Search Tree**                | :fire: In Progress |
| **N Ary Tree**                        | :boom: Not Started |
| **Segment Tree**                      | :boom: Not Started |
| **Interval Tree**                     | :boom: Not Started |
| **Trie**                              | :boom: Not Started |

## Binary Tree APIs

### Sample Usage 
Click **[Here](docs/BinaryTree.md)** for **Full Binary Tree Doc & Code Snippets**

**Construct a binary Tree**
```python
from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

tree = BinaryTree(root=a)
```

**Pretty print a binary tree**
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

**View binary tree properties**

```python
print('Tree Height   : ', tree.getHeight())
print('Number Leaves : ', tree.getNumberLeaves())
print('Is Balanced   : ', tree.isBalanced())
print('Is BST        : ', tree.isBinarySearchTree())
print('Is Symmetric  : ', tree.isSymmetric())
```
```
Tree Height   :  3
Number Leaves :  4
Is Balanced   :  True
Is BST        :  False
Is Symmetric  :  False
```
**Compare 2 binary tree**
```python
tree_a = BinaryTree(root=a)
tree_b = BinaryTree(root=b)

print("a and b are same tree? :", tree_a.isSameTree(tree_b))
print("a is subtree of b?     :", tree_a.isSubTreeOf(tree_b))
print("b is subtree of a?     :", tree_b.isSubTreeOf(tree_a))
```
```
a and b are same tree? : False
a is subtree of b?     : False
b is subtree of a?     : True
```