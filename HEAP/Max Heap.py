from typing import List, Any


class Heap:
    def __init__(self, a: List[Any] = None):
        self.n = len(a) if a else 0
        self.heap = a if a else []
        self.heapify()

    def heapify(self):
        # start from the latest parent and heapify the input list
        for i in range((self.n - 2) // 2, -1, -1):
            self.bubble_down(self.n, i)

    def bubble_down(self, n, index: int):
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

    def bubble_up(self, index, debug=False):
        parent = index // 2

        if parent >= 0 and self.heap[index] > self.heap[parent]:
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

    def get_max(self):
        return self.pop()

    def insert(self, item, debug=False):
        self.heap.append(item)
        self.n += 1
        if self.n > 1:
            self.bubble_up(self.n - 1)

        if debug: print(f"current heap: {self.heap}")

        return self.n

    def sort(self):
        for i in range(self.n - 1, 0, -1):
            self.swap(0, i)
            self.bubble_down(i, 0)

    def get_heap(self):
        return self.heap


def main():
    arr = [1, 6, 3, 5, 8, 4, 7, 2]
    print(f"original arr: {arr}")
    h = Heap(arr)
    h.sort()
    print(f"sorted arr: {arr}")

    # demo pop
    arr = [2, 5, 9, 5, 3, 7, 1]
    h = Heap(arr)
    max_value = h.pop()
    print(f"arr after 1 pop: {arr}")

    # demo empty arr and insertion
    h2 = Heap()
    arr = [2, 5, 9, 5, 3, 7, 1]
    for item in arr:
        h2.insert(item, debug=True)

    heap = h2.get_heap()
    print(f"Final heap after multiple insertions: {heap}")

    # Now sort
    h2.sort()
    sorted_arr = h2.get_heap()
    print(f"Sorted: {sorted_arr}")


if __name__ == "__main__":
    main()


