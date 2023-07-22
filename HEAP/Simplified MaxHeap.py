from typing import List, Any

# Class to represent a max heap
class Heap:
    # Initialize the heap
    def __init__(self, a: List[Any] = None):
        # Set heap to provided list or empty list
        self.heap = a if a else []
        # Build the max heap from the input list
        self.heapify()

    # Method to turn the list into a max heap
    def heapify(self):
        # Start from the last parent node and bubble down
        for i in reversed(range(len(self.heap) // 2)):
            self.bubble_down(len(self.heap), i)

    # Method to maintain heap property for a node at a specific index
    def bubble_down(self, n, index):
        # Assume the current node is the largest
        largest = index
        # Compute the indices of the left and right children
        left = 2 * index + 1
        right = 2 * index + 2

        # If the left child is larger, update the largest node
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        # If the right child is larger, update the largest node
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        # If the largest node is not the current node, swap and bubble down again
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(n, largest)

    # Method to restore heap property after insertion
    def bubble_up(self, index):
        # Compute the parent node's index
        parent = (index - 1) // 2
        # If the parent node is less than the current node, swap them
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.swap(index, parent)
            # Continue to bubble up
            self.bubble_up(parent)

    # Method to swap two nodes
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Method to remove and return the maximum element
    def pop(self):
        if len(self.heap) > 1:
            # Swap root with the last node
            self.swap(0, len(self.heap) - 1)
            # Remove the last node and save it to return later
            max_value = self.heap.pop()
            # Bubble down the root node
            self.bubble_down(len(self.heap), 0)
            return max_value
        elif self.heap:
            # If the heap only has one element, return it
            return self.heap.pop()

    # Method to return the maximum element
    def get_max(self):
        return self.pop()

    # Method to insert a new element
    def insert(self, item):
        # Add the new item at the end
        self.heap.append(item)
        # Bubble it up to its correct position
        self.bubble_up(len(self.heap) - 1)

    # Method to sort the heap
    def sort(self):
        sorted_heap = []
        # Continuously remove the max and append it to the result list
        while self.heap:
            sorted_heap.append(self.pop())
        # Update the heap with the sorted list
        self.heap = sorted_heap
        return self.heap

    # Method to get the current heap
    def get_heap(self):
        return self.heap

# Driver code
def main():
    arr = [1, 6, 3, 5, 8, 4, 7, 2]
    # Initialize a heap and build it
    h = Heap(arr)
    print(f"heap after build: {h.get_heap()}")

    # Pop operation
    max_value = h.pop()
    print(f"heap after 1 pop: {h.get_heap()}")

    # Insert operation
    h.insert(9)
    print(f"heap after insertion: {h.get_heap()}")

    # Sort operation
    sorted_heap = h.sort()
    print(f"heap after sorting: {sorted_heap}")

if __name__ == "__main__":
    main()
    