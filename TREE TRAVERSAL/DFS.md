## Depth First Search

- Depth-first search (DFS) is a method for exploring a tree or graph. In a DFS, you start at a root node and and then explore as far as possible along each branch before going back. Go as left a possible and we backtrack when we reach a dead end.

- Depth First Search (DFS) is a method for traversing or searching tree or graph data structures. It starts at the root (for a tree) or an arbitrary node (for a graph), and explores as far as possible along each branch before backtracking.

# There are 3 types of DFS 

- PreOrder = In this type of traversal, the process is: root node --> left subtree --> right subtree. The root is visited first, then the left subtree, and finally the right subtree.

- PostOrder = The order of traversal here is: left subtree --> root node --> right subtree. That means the left subtree is visited first, then the root, and finally the right subtree. This traversal method is only applicable to binary trees, and when applied, it gives nodes in non-decreasing order.

- InOrder = In this traversal, the order is: left subtree --> right subtree --> root node. The root is visited last, after the left and right subtrees.

