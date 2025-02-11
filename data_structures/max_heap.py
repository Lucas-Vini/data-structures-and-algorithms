from heap import Heap

class MaxHeap(Heap):
    def _max_heapify(self, i: int):
        largest = i
        left = self._left(i)
        rigth = self._right(i)

        if (left < self.heap_size) and (self.heap[left] > self.heap[i]):
            largest = left
        
        if (rigth < self.heap_size) and (self.heap[rigth] > self.heap[i]):
            largest = rigth

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(i)

    def build_max_heap(self, heap: list):
        self.heap = heap
        self.heap_size = len(heap)
        for i in range(self.heap_size // 2, -1, -1):
            self._max_heapify(i)

my_heap = MaxHeap()
my_heap.build_max_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

print(my_heap.heap)
