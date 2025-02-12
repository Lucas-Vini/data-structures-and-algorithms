from data_structures.max_heap import MaxHeap

def heap_sort(elements: list):
    heap = MaxHeap()
    heap.build_max_heap(elements)
    for i in range(len(elements) - 1, 2, -1):
        heap.heap[1], heap.heap[i] = heap.heap[i], heap.heap[1]
        heap.heap_size -= 1
        heap.max_heapify(1)
    return heap.heap


a = [2, 6, 1, 8, 3, 1, 6, 3, 9]

print(heap_sort(a))
