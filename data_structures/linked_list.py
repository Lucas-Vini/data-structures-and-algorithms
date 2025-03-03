from node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._length = 0

    def append(self, value):
        if self.first:
            self.last.next = Node(value)
            self.last = self.last.next
        else:
            self.first = Node(value)
            self.last = self.first
        self._length += 1

    def __len__(self):
        return self._length
    
    def __getitem__(self, index):
        pointer = self.first
        for i in range(index):
            if not pointer.next:
                raise IndexError("list index out of range")
            pointer = pointer.next
        if not pointer:
            raise IndexError("list index out of range")
        return pointer.value

    def __setitem__(self, index, value):
        pointer = self.first
        for i in range(index):
            if not pointer.next:
                raise IndexError("list index out of range")
            pointer = pointer.next
        if not pointer:
            raise IndexError("list index out of range")
        pointer.value = value

    def index(self, value):
        pointer = self.first
        index = 0
        while pointer:
            if pointer.value == value:
                return index
            pointer = pointer.next
            index += 1
        raise ValueError(f"{value} is not in list")
    
    def insert(self, index, value):
        if index == 0:
           self.first = Node(value, self.first)
        elif index == self._length - 1:
            self.append(value)
        else:
            pointer = self.first
            for i in range(index - 1):
                if not pointer.next:
                    raise IndexError("list index out of range")
                pointer = pointer.next
            pointer.next = Node(value, pointer.next)


