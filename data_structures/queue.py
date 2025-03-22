from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length
    
    def __repr__(self):
        string_list = "["
        pointer = self.head
        for i in range(len(self)):
            string_list += str(pointer.value)
            pointer = pointer.next
            if pointer:
                string_list += ", "

        string_list += "]"
        return string_list
    
    def enqueue(self, value):
        if self._length == 0:
            self.tail = Node(value)
            self.head = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self._length += 1

    def dequeue(self):
        if not self.head:
            raise IndexError("empty stack")
    
        head_value = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = self.head

        self._length -= 1
        return head_value
