class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]