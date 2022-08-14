class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            

bst1 = Node(-10)
bst2 = Node(9)
bst3 = Node(20)
bst4 = Node(15)
bst5 = Node(7)

bst1.left = bst2
bst1.right = bst3

bst3.left = bst4
bst3.right = bst6

bst4.left = bst5

bst5.left = bst9

bst6.right = bst7

bst7.right = bst8

