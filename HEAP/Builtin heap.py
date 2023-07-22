import heapq as hq

if __name__ == "__main__":
    values = [22, 4, 8, 45, 14, 4]

    hq.heapify(values)
    min_heap = values

    print("Popping all items from the max-heap results in a Descending order")
    while min_heap:
        print(hq.heappop(min_heap))
