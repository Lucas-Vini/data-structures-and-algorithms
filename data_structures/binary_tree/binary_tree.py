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
            print('(', end='')
            self.inorder_traversal(node.left)
        print(node.value, end='')
        if node.right:
            self.inorder_traversal(node.right)
            print(')', end='')

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

        
        


my_tree = BinaryTree()

n1 = TreeNode('1')
n2 = TreeNode('N')
n3 = TreeNode('5')
n4 = TreeNode('C')
n5 = TreeNode('R')
n6 = TreeNode('3')
n7 = TreeNode('V')
n8 = TreeNode('4')
n9 = TreeNode('5')
n0 = TreeNode('3')

n0.left = n6
n0.right = n9
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.left = n8
n8.right = n7
my_tree.root = n0

print(my_tree.height())
