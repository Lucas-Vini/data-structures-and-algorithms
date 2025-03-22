from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length