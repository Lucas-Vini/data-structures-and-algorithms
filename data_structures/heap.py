class Heap():
    def __init__(self):
        self.heap = []
        self.heap_size = 0 

    def _parent(self, i):
        return (i - 1) // 2
    
    def _left(self, i):
        return (i * 2) + 1
    
    def _right(self, i):
        return (i * 2) + 2