class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            

bst1 = Node(1)
bst2 = Node(2)
bst3 = Node(3)
bst4 = Node(4)
bst5 = Node(5)
bst6 = Node(6)
bst7 = Node(7)
bst8 = Node(8)
bst9 = Node(9)

bst1.left = bst2
bst1.right = bst3

bst3.left = bst4
bst3.right = bst6

bst4.left = bst5

bst5.left = bst9

bst6.right = bst7

bst7.right = bst8

