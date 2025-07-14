from data_structures.queue import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value=None, node=None):
        self.root = None
        if node:
            self.root = node
        elif value:
            root_node = TreeNode(value)
            self.root = root_node

    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.in_order_traversal(node.left)
        print(node.value, end=' ')
        if node.right:
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.post_order_traversal(node.left)
        if node.right:
            self.post_order_traversal(node.right)
        print(node.value)

    def height(self, node=None):
        left_height = 0
        right_height = 0

        if node is None:
            node = self.root

        if node.left:
            left_height = self.height(node.left)
        if node.right:
            right_height = self.height(node.right)

        return max(left_height, right_height) + 1
    
    def level_order_traversal(self, node=None):
        if node is None:
            node = self.root
        
        queue = Queue()
        queue.enqueue(node)

        while len(queue):
            current_node = queue.dequeue()
            
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

            print(current_node.value)