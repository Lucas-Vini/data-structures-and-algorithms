from heap import Heap

class MinHeap(Heap):
    def _min_heapify(self, i: int):
        smallest = i
        left = self._left(i)
        rigth = self._right(i)

        if (left < self.heap_size) and (self.heap[left] < self.heap[i]):
            smallest = left
        
        if (rigth < self.heap_size) and (self.heap[rigth] < self.heap[smallest]):
            smallest = rigth

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    def build_min_heap(self, heap: list):
        self.heap = heap
        self.heap_size = len(heap)
        for i in range(self.heap_size // 2, -1, -1):
            self._min_heapify(i)
