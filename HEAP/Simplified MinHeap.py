from typing import List, Any

class MinHeap:
    def __init__(self, a: List[Any] = None):
        self.heap = a if a else []
        self.heapify()

    def heapify(self):
        for i in range(len(self.heap)//2, -1, -1):
            self.bubble_down(i)

    def bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.bubble_down(smallest)

    def bubble_up(self, index):
        parent = (index - 1) // 2
        if index and self.heap[parent] > self.heap[index]:
            self.swap(parent, index)
            self.bubble_up(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        if self.heap:
            self.bubble_down(0)
        return value

    def get_min(self):
        return self.pop()

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(len(self.heap) - 1)

    def sort(self):
        size = len(self.heap)
        for i in range(size - 1, 0, -1):
            self.swap(i, 0)
            self.bubble_down(i)

    def get_heap(self):
        return self.heap
