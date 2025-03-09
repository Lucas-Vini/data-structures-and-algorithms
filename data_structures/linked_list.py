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
    
    def __getitem__(self, index: int):
        pointer = self._get_node(index)
        if not pointer:
            raise IndexError("list index out of range")
        return pointer.value

    def __setitem__(self, index: int, value):
        pointer = self._get_node(index)
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
    
    def insert(self, index: int, value):
        if index == 0:
           self.first = Node(value, self.first)
        elif index == self._length:
            self.append(value)
        else:
            pointer = self._get_node(index - 1)
            pointer.next = Node(value, pointer.next)
        self._length += 1

    def remove(self, value):
        if not self.first:
            raise ValueError(f"{value} is not in list")
        
        if self.first.value == value:
            self.first = self.first.next
            if not self.first:
                self.last = self.first
        
        pointer = self.first
        while pointer.next:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                if not pointer.next:
                    self.last = pointer.next

    def _get_node(self, index: int):
        pointer = self.first
        for i in range(index):
            if not pointer.next:
                raise IndexError("list index out of range")
            pointer = pointer.next
        return pointer

    def __repr__(self):
        string_list = "["
        pointer = self.first
        for i in range(len(self)):
            string_list += str(pointer.value)
            pointer = pointer.next
            if pointer:
                string_list += ","

        string_list += "]"
        return string_list



ele = LinkedList()
print(ele, len(ele))
ele.append(1)
print(ele, len(ele))
ele.append(11)
print(ele, len(ele))
print(ele[1], ele[0])
ele[0] = 22
print(ele, len(ele))
print(ele[1], ele[0])
print(ele)
print(ele.index(11))
print(ele.index(22))
ele.insert(0, 33)
print(ele, len(ele))
ele.insert(2, 9)
print(ele, len(ele))
ele.insert(4, 4)
print(ele, len(ele))