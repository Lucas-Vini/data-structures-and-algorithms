class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value=None):
        self.root = None
        if value:
            root_node = TreeNode(value)
            self.root = root_node

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.inorder_traversal(node.left)
        print(node.value, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
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

