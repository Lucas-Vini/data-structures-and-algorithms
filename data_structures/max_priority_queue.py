from data_structures.max_heap import MaxHeap

class MaxPriorityQueue(MaxHeap):
    def heap_maximum(self):
        return self.heap[0]