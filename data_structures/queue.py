from node import Node

class Queue:
    '''A class to create a queue'''
    def __init__(self):
        self.first = None
        self.last = None
        self._length = 0

    def enqueue(self, item):
        '''Add an item to the end of the queue'''
        new_node = Node(item)
        if self.last:
            self.last.next = new_node
            self.last = new_node
        else:
            self.last = new_node
            self.first = new_node
        self._length += 1

    def dequeue(self):
        '''Remove and return the fisrt item in the queue'''
        if self.first:
            item = self.first.data
            self.first = self.first.next
            self._length -= 1
            if self._length == 0:
                self.last = None
            return item
        else:
            raise IndexError('queue is empty')

    def peek(self):
        '''Peek the fisrt item in the queue'''
        if self.first:
            return self.first.data
        else:
            raise IndexError('queue is empty')
        
    def __repr__(self):
        '''List representation with a string'''
        representation = ""
        current_node = self.first
        while current_node:
            representation += str(current_node.data) + " -> "
            current_node = current_node.next
        return representation

    def __str__(self):
        '''List representation with a string'''
        return self.__repr__()

    def __len__(self):
        '''Return the lenght of the list'''
        return self._length
