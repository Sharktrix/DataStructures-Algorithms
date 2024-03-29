## Binary Search Tree 
- All values in the left subtree < all values in the right subtree
- BST structure means that the root always holds the middle point in a sorted elements.
- Think of BST as a way to bring the power of binary search (i.e, runtime of O(logn)) to linked structures! 
- NOTE: We have to ensure that the BST is height-balanced to hold the proper runtime (week12)
- Expected Runtime: O(log n), worst runtime: O(n)

## Searching in BST 

- Compare target with value at root, if equal return true. 
- If target smaller than root, look into the right subtree.
- If target larger than root, look into the right subtree.
- Recurse until found or return none if no more child.
- 

## Insertion in BST 

- Compare item with value at root, if no root insert as root.
- If item smaller than root, look into the left subtree
- If item larger than root, look into the right subtree.
- Recurse

## Deletion from BST 

- Case 0: Key to be deleted does not exist: return not found 
- Case 1: Key to be deleted is a leaf: just delete the node
- Case 2: Key to be deleted has one child:

- Delete item 
- Make the parent of item, to be the parent of the child of item.

- Case 3: 
- Key to be deleted has two children :
- find the greatest value which is strictly smaller than the item.
- This would mean the right most node in the left subtree of the item.
- Finds you a node which either has __NO__ child or has only __LEFT__ child 
  - if no child, then just do a swap and delete
  - if no child do swap and delete as well as what was done as part of delete for case 2 

OR 




