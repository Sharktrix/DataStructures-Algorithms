from typing import List, Optional

class BinSearchTree(object):
    # Define a class Node to represent a node in the binary search tree
    class Node:
        def __init__(self, value, left=None, right=None):
            # The value stored in the node
            self.value = value
            # The left child of the node
            self.left = left
            # The right child of the node
            self.right = right

    def __init__(self, values: List = None):
        # values is an optional list of elements to insert into the tree at initialization
        self.values = values
        # The root node of the binary search tree
        self.root = None
        # The total number of nodes in the tree
        self.n = len(values) if values else 0
        # Insert the given values into the tree, if any
        if values:
            for v in values:
                self.insert(v)

    def insert(self, data):
        # Insert a new value into the tree
        # If the tree is empty, the new node becomes the root
        if self.root is None:
            self.root = self.Node(data)
        else:
            # If the tree is not empty, we need to find the right place to insert the new node
            current = self.root
            inserted = False

            while not inserted:
                if data < current.value:  # Looking at the left subtree
                    if current.left is not None:
                        current = current.left  # Go to the left child
                    else:  # If there's no left child, insert here and stop the loop
                        current.left = BinSearchTree.Node(data)
                        inserted = True
                else:  # Looking at the right subtree
                    if current.right is not None:
                        current = current.right  # Go to the right child
                    else:  # If there's no right child, insert here and stop the loop
                        current.right = BinSearchTree.Node(data)
                        inserted = True

    def search(self, data):
        # Search for a value in the tree
        # Start the search from the root
        current = self.root

        while current is not None:
            if data < current.value:  # Go to the left subtree
                current = current.left
            elif data > current.value:  # Go to the right subtree
                current = current.right
            else:  # If the value is equal to the target, return True
                return True

        return False  # If we've searched the entire tree and haven't found the value, return False

    # As a practice, please implement this!
    def remove(self, data):
        # TODO: Implement this method to remove a node from the tree
        pass

    def _sorted_array_to_bst(self, nums, start, end):
        """
        Given a sorted array, converts it into a balanced binary search tree.
        """
        if end < start:
            return None

        mid = (start + end) // 2
        node = self.Node(nums[mid])

        # The left subtree is formed by the elements in the array before the middle element
        node.left = self._sorted_array_to_bst(nums, start, mid - 1)
        # The right subtree is formed by the elements in the array after the middle element
        node.right = self._sorted_array_to_bst(nums, mid + 1, end)
        return node

    def sorted_array_to_bst(self, nums: List[int]) -> Optional[Node]:
        # Public method to convert a sorted array into a binary search tree
        return self._sorted_array_to_bst(nums, start=0, end=len(nums) - 1)


def main():
    nums = [12, 34, 9, 8, 18, 45, 90, 4, 43, 13, 5, 2]
    # Create a binary search tree and insert the numbers in 'nums'
    bst = BinSearchTree(nums)

    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Create a binary search tree from a sorted array
    bst1 = BinSearchTree()
    bst1 = bst1.sorted_array_to_bst(nums1)

    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # Create another binary search tree from a sorted array
    bst2 = BinSearchTree()
    bst2 = bst2.sorted_array_to_bst(nums2)
    target = 10
    # Search for a target value in the binary search tree


if __name__ == "__main__":
    main()
