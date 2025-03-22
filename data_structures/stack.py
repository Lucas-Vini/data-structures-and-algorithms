from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __len__(self):
        return self._length
    
    def __repr__(self):
        string_list = "["
        pointer = self.top
        for i in range(len(self)):
            string_list += str(pointer.value)
            pointer = pointer.next
            if pointer:
                string_list += ", "

        string_list += "]"
        return string_list
    
    def push(self, value):
        self.top = Node(value, self.top)
        self._length += 1

    def pop(self):
        if self._length > 0:
            top_value = self.top.value
            self.top = self.top.next
            self._length -= 1
            return top_value
        raise IndexError("empty stack")

    def peek(self):
        if self._length > 0:
            return self.top.value
        raise IndexError("empty stack")
