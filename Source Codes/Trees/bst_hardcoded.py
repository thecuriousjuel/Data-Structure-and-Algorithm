class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


bst3 = Node(3)
bst5 = Node(5)
bst1 = Node(1)
bst6 = Node(6)
bst2 = Node(2)
bst0 = Node(0)
bst8 = Node(8)
bst7 = Node(7)
bst4 = Node(4)
bst9 = Node(9)

bst3.left = bst5
bst3.right = bst1

bst5.left = bst6
bst5.right = bst2

bst2.left = bst7
bst2.right = bst4

bst1.left = bst0
bst1.right = bst8

bst6.left = bst9



