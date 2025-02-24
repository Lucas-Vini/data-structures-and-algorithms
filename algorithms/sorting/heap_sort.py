from data_structures.heap.max_heap import MaxHeap
from data_structures.heap.min_heap import MinHeap

def heap_sort(elements: list, reverse=False):
    if reverse:
        heap = MinHeap()
        heap.build_min_heap(elements)
    else:
        heap = MaxHeap()
        heap.build_max_heap(elements)

    for i in range(len(elements) - 1, 0, -1):
        heap.heap[0], heap.heap[i] = heap.heap[i], heap.heap[0]
        heap.heap_size -= 1

        if reverse:
            heap.min_heapify(0)
        else:
            heap.max_heapify(0)
    return heap.heap

