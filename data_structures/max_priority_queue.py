from data_structures.max_heap import MaxHeap

class MaxPriorityQueue(MaxHeap):
    def heap_maximum(self):
        return self.heap[0]
    
    def heap_extract_max(self):
        if self.heap_size < 1:
            raise Exception("Heap underflow.")
        
        max = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i: int, key):
        if key < self.heap[i]:
            raise Exception("New key is smaller than current key")
        
        self.heap[i] = key
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.heap[self.heap_size - 1] = key
        self.heap_increase_key(self.heap_size - 1, key)