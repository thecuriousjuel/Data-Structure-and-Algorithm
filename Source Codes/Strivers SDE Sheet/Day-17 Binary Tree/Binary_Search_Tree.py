class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class BST:
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



bst = BST()
bst.add_node(5)
bst.add_node(15)
bst.add_node(51)
bst.add_node(25)
bst.add_node(48)
bst.add_node(66)
bst.add_node(95)
bst.add_node(57)
bst.add_node(35)
