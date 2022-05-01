# pytree - A Rich Tree API Implemented in Python
<!-- TOC start -->
- [Binary Tree API](#binary-tree-api)
  * [Build a binary tree](#build-a-binary-tree)
  * [Traversal a binary tree](#traversal-a-binary-tree)
  * [Check binary tree properties](#check-binary-tree-properties)
  * [Build binary tree from traversal orders](#build-binary-tree-from-traversal-orders)
<!-- TOC end -->
<!-- TOC --><a name="binary-tree-api"></a>
## Binary Tree API

<!-- TOC --><a name="build-a-binary-tree"></a>
### Build a binary tree
```python
from tree.BinaryTree import BinaryTree
from node.BinaryTreeNode import BinaryTreeNode

a, b, c, d, e, f, g = (BinaryTreeNode(i) for i in range(7))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

tree = BinaryTree(root=a)
tree.pprint()
```

```
  _0_  
 /   \ 
 1   2 
/ \ / \
3 4 5 6
```

<!-- TOC --><a name="traversal-a-binary-tree"></a>
### Traversal a binary tree
```python
for node in tree.preorder():
    print(node.val, '|', node)
for node in tree.inorder():
    print(node.val, '|', node)
for node in tree.postorder():
    print(node.val, '|', node)
```
```python
# preorder
0 | BinaryTreeNode(0, left=1, right=2)
1 | BinaryTreeNode(1, left=3, right=4)
3 | BinaryTreeNode(3, left=None, right=None)
4 | BinaryTreeNode(4, left=None, right=None)
2 | BinaryTreeNode(2, left=5, right=6)
5 | BinaryTreeNode(5, left=None, right=None)
6 | BinaryTreeNode(6, left=None, right=None)
# Inorder
3 | BinaryTreeNode(3, left=None, right=None)
1 | BinaryTreeNode(1, left=3, right=4)
4 | BinaryTreeNode(4, left=None, right=None)
0 | BinaryTreeNode(0, left=1, right=2)
5 | BinaryTreeNode(5, left=None, right=None)
2 | BinaryTreeNode(2, left=5, right=6)
6 | BinaryTreeNode(6, left=None, right=None)
# Postorder
3 | BinaryTreeNode(3, left=None, right=None)
4 | BinaryTreeNode(4, left=None, right=None)
1 | BinaryTreeNode(1, left=3, right=4)
5 | BinaryTreeNode(5, left=None, right=None)
6 | BinaryTreeNode(6, left=None, right=None)
2 | BinaryTreeNode(2, left=5, right=6)
0 | BinaryTreeNode(0, left=1, right=2)
```

<!-- TOC --><a name="check-binary-tree-properties"></a>
### Check binary tree properties
```python
print('Tree Height  : ', tree.height())
print('Is Balanced  : ', tree.isBalanced())
print('Num Leaves   : ', tree.getNumLeaves())
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

<!-- TOC --><a name="build-binary-tree-from-traversal-orders"></a>
### Build binary tree from traversal orders
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