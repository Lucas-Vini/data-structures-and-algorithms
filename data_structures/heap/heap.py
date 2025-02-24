class Heap():
    def __init__(self):
        self.heap = []
        self.heap_size = 0 

    def _parent(self, i: int):
        return (i - 1) // 2
    
    def _left(self, i: int):
        return (i * 2) + 1
    
    def _right(self, i: int):
        return (i * 2) + 2