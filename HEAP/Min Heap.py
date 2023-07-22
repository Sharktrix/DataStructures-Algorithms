from typing import List, Any

class MinHeap:
    def __init__(self, a: List[Any] = None):
        self.n = len(a) if a else 0
        self.heap = a if a else []
        self.heapify()

    def heapify(self):
        for i in range((self.n - 2) // 2, -1, -1):
            self.bubble_down(self.n, i)

    def bubble_down(self, n, index: int):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.bubble_down(n, smallest)

    def bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.bubble_up(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        value = None
        if self.n == 1:
            value = self.heap.pop()
        elif self.n > 1:
            self.swap(0, self.n - 1)
            value = self.heap.pop()
            self.n -= 1
            self.bubble_down(self.n, 0)
        return value

    def get_min(self):
        return self.pop()

    def insert(self, item):
        self.heap.append(item)
        self.n += 1
        if self.n > 1:
            self.bubble_up(self.n - 1)

    def sort(self):
        for i in range(self.n - 1, 0, -1):
            self.swap(0, i)
            self.bubble_down(i, 0)

    def get_heap(self):
        return self.heap

def main():
    arr = [1, 6, 3, 5, 8, 4, 7, 2]
    print(f"original arr: {arr}")
    h = MinHeap(arr)
    h.sort()
    print(f"sorted arr: {arr}")

    arr = [2, 5, 9, 5, 3, 7, 1]
    h = MinHeap(arr)
    min_value = h.pop()
    print(f"arr after 1 pop: {arr}")

    h2 = MinHeap()
    arr = [2, 5, 9, 5, 3, 7, 1]
    for item in arr:
        h2.insert(item)

    heap = h2.get_heap()
    print(f"Final heap after multiple insertions: {heap}")

    h2.sort()
    sorted_arr = h2.get_heap()
    print(f"Sorted: {sorted_arr}")

if __name__ == "__main__":
    main()


#The main difference is in bubble_down and bubble_up functions. We now compare if the child is smaller than the parent (or if one child is smaller than the other) instead of larger. Accordingly, get_max is now get_min since we’re dealing with a min heap. The sort function still works, but it now sorts the array in descending order.
