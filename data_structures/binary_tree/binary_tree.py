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