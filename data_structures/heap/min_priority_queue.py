from data_structures.heap.min_heap import MinHeap

class MinPriorityQueue(MinHeap):
    def heap_minimum(self):
        return self.heap[0]
    
    def heap_extract_min(self):
        if self.heap_size < 1:
            raise Exception("Heap underflow.")
        
        min = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heapify(0)
        return min

    def heap_decrease_key(self, i: int, key):
        if key > self.heap[i]:
            raise Exception("New key is smaller than current key")
        
        self.heap[i] = key
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def min_heap_insert(self, key):
        self.heap_size += 1
        self.heap.append(key)
        self.heap_decrease_key(self.heap_size - 1, key)
