from node import Node

class Stack:
    '''Class to create a new empty stack'''
    def __init__(self):
        self.top = None
        self._length = 0

    def push(self, item):
        '''Method to push a new item'''
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._length += 1

    def pop(self):
        '''Method to pop the item at the top'''
        if self.top != None:
            item = self.top.data
            self.top = self.top.next
            self._length -= 1
            return item
        else:
            raise IndexError('pop from empty stack')
        
    def peek(self):
        '''Method to peek the item at the top'''
        if self.top != None:
            return self.top.data
        else:
            raise IndexError('stack is empty')
        

    def __len__(self):
        '''Method to return the lenght of the list'''
        return self._length

    def __repr__(self):
        '''Stack representation with a string'''
        representation = ""
        current_node = self.top
        while current_node:
            representation += str(current_node.data) + "\n"
            current_node = current_node.next
        return representation

    def __str__(self):
        '''Stack representation with a string'''
        return self.__repr__()
        
