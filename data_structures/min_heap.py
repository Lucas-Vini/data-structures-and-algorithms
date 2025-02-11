from heap import Heap

class MinHeap(Heap):
    def _min_heapify(self, i):
        smallest = i
        left = self._left(i)
        rigth = self._right(i)

        if (left <= self.heap_size) and (self.heap[left] < self.heap[i]):
            smallest = left
        
        if (rigth <= self.heap_size) and (self.heap[rigth] < self.heap[i]):
            smallest = rigth

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._max_heapify(i)