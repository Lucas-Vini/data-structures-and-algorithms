class Node:
    '''Class to create a new Node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''Class to create a new empty linked list'''
    def __init__(self):
        self.head = None
        self._length = 0

    def _go_to_node(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            if current_node == None:
                raise IndexError("list index out of range")
        if current_node:
            return current_node
        else:
            raise IndexError("list index out of range")

    def append(self, item):
        '''Method to append a new item to the end of the list'''
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(item)
        else:
            self.head = Node(item)
        self._length += 1

    def __len__(self):
        '''Method to return the lenght of the list'''
        return self._length
        
    def __getitem__(self, index):
        '''Method to access an item in the list'''
        current_node = self._go_to_node(index)
        return current_node.data
                
    def __setitem__(self, index, item):
        '''Method to modify an item in the list'''
        current_node = self._go_to_node(index)
        current_node.data = item

    def index(self, item):
        '''Method to search for an item in the list'''
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == item:
                return index
            current_node = current_node.next
            index += 1
        raise ValueError("{} is not in list".format(item))

    def __add__(self, other_list):
        '''Method to concatenate two linked lists'''
        if type(self) == type(other_list):
            result = LinkedList()
            current_node = self.head
            while current_node:
                result.append(current_node.data)
                current_node = current_node.next
            current_node = other_list.head
            while current_node:
                result.append(current_node.data)
                current_node = current_node.next
            return result
        else:
            raise TypeError("unsupported operand type")
                
    def __repr__(self):
        '''List representation with a string'''
        representation = "Head -> "
        current_node = self.head
        while current_node:
            representation += str(current_node.data) + " -> "
            current_node = current_node.next
        return representation

    def __str__(self):
        '''List representation with a string'''
        return self.__repr__()

    def insert(self, index, item):
        '''Method to insert an item in the list'''
        new_node = Node(item)    
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:                       
            current_node = self._go_to_node(index-1)
            new_node.next = current_node.next
            current_node.next = new_node

    def remove(self, item):
        '''Method to remove an item of the list'''
        if self.head == None:
            raise ValueError("{} is not in list".format(item))
        if self.head.data == item:
            self.head = self.head.next
        else:
            previous_node = self.head
            current_node = self.head.next
            while current_node:
                if current_node.data == item:
                    break
                previous_node = current_node
                current_node = current_node.next
            if current_node:
                previous_node.next = current_node.next
                current_node.next = None
            else:
                raise ValueError("{} is not in list".format(item))
