from typing import List, Any

class Heap:
    def __init__(self, a: List[Any] = None):
        self.heap = a if a else []
        self.heapify()

    def heapify(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.bubble_down(len(self.heap), i)

    def bubble_down(self, n, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(n, largest)

    def bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.swap(index, parent)
            self.bubble_up(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        if len(self.heap) > 1:
            self.swap(0, len(self.heap) - 1)
            max_value = self.heap.pop()
            self.bubble_down(len(self.heap), 0)
            return max_value
        elif self.heap:
            return self.heap.pop()

    def get_max(self):
        return self.pop()

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(len(self.heap) - 1)

    def sort(self):
        sorted_heap = []
        while self.heap:
            sorted_heap.append(self.pop())
        self.heap = sorted_heap
        return self.heap

    def get_heap(self):
        return self.heap

def main():
    arr = [1, 6, 3, 5, 8, 4, 7, 2]
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
