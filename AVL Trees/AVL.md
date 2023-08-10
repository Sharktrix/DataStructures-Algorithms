## Definition: 

It is a binary search tree for which we always ensure the tree maintains a height balance during insertion and deletion. In order to achieve this we make note of the height information for all nodes.
- A type of Balance BST
- They ensure that the tree stays height-balanced after every operation
- This is achieved by storing the height information of each node with its data
- This way we do not have to recalculate the heights at each operation
- hight-balance= right-height - left-hight




## Operations on AVL Tree:
Search
Exactly like what we have done in BST

### Insertion:

Search and insert a leaf the same way we did for BST
New node is a leaf and thus will have a height balance of 0
Fix height balance
Go back to the parent and adjust the height balance.
If the height balance of a node is ever more than 1 or less than -1 (abs(height)>1), the subtree at that node will have to go through a rotation in order to fix the height balance. The process continues until we are back to the root.
NOTE: The adjustment must happen from the bottom up

### Deletion
Follow the same steps taken in BST deletion
node is leaf
node has one child
node has two child-find in-order successor
Fix height balance