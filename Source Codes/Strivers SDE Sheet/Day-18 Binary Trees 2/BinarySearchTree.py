class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
    def add_node_helper(self, root, new_node):
        if new_node.data < root.data:
            if root.left == None:
                root.left = new_node
            else:
                self.add_node_helper(root.left, new_node)
        else:
            if root.right == None:
                root.right = new_node
            else:
                self.add_node_helper(root.right, new_node)
                                 
    
    def add_node(self, data):
        new_node = Node(data)
        
        if self.root == None:
            self.root = new_node
        else:
            self.add_node_helper(self.root, new_node)
                                 
                                 
bst = BinarySearchTree()
bst.add_node(45)
bst.add_node(21)
bst.add_node(10)
bst.add_node(15)
bst.add_node(72)
bst.add_node(36)
bst.add_node(88)
bst.add_node(92)
bst.add_node(76)
bst.add_node(43)
bst.add_node(74)
                                 
                                 
                                 