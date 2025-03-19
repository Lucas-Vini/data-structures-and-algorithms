from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __len__(self):
        return self._length