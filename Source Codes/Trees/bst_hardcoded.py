class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


bst1 = Node(50)
bst2 = Node(7)
bst3 = Node(2)
bst4 = Node(3)
bst5 = Node(5)
bst6 = Node(1)
bst7 = Node(30)

bst1.left = bst2
bst1.right = bst3

bst2.left = bst4
bst2.right = bst5

bst3.left = bst6
bst3.right = bst7



