from data_structures.binary_tree.binary_tree import BinaryTree, TreeNode

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        parent_node = None
        current_node = self.root

        while current_node:
            parent_node = current_node
            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        if parent_node.value > value:
            parent_node.left = TreeNode(value)
        else:
            parent_node.right = TreeNode(value)

    def search(self, value):
        return self._search(value, node=self.root)
    
    def _search(self, value, node):
        if node.value == value:
            return BinarySearchTree(node=node)
        
        if node is None:
            return None
        
        if value < node.value:
            return self._search(value, node.left)
        return self._search(value, node.right)

