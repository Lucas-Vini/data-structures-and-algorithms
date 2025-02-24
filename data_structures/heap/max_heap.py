from data_structures.heap import Heap

class MaxHeap(Heap):
    def max_heapify(self, i: int):
        largest = i
        left = self._left(i)
        rigth = self._right(i)

        if (left < self.heap_size) and (self.heap[left] > self.heap[i]):
            largest = left
        
        if (rigth < self.heap_size) and (self.heap[rigth] > self.heap[largest]):
            largest = rigth

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self, heap: list):
        self.heap = heap
        self.heap_size = len(heap)
        for i in range(self.heap_size // 2, -1, -1):
            self.max_heapify(i)
