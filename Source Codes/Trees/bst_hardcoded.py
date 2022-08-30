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
bst10 = Node(10)

bst1.left = bst2
bst1.right = bst3

bst2.left = bst4
bst2.right = bst5

bst3.right = bst6

#bst5.left = bst6

#bst3.right = bst7

