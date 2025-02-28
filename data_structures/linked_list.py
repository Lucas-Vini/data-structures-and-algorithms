from node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def append(self, value):
        if self.first:
            self.last.next = Node(value)
            self.last = self.last.next
        else:
            self.first = Node(value)
            self.last = self.first
        self.length += 1

    def __len__(self):
        return self.length
