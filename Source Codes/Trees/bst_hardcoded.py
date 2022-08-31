class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            

# bst100 = Node(100)
# bst50 = Node(50)
# bst25 = Node(25)
# bst75 = Node(75)
# bst150 = Node(150)
# bst140 = Node(140)
# bst200 = Node(200)
# bst30 = Node(30)
# bst70 = Node(70)
# bst80 = Node(80)
# bst85 = Node(85)


# bst100.left = bst50
# bst100.right = bst150

# bst50.left = bst25
# bst50.right = bst75

# bst25.right = bst30

# bst30.right = bst85

# bst75.left = bst70
# bst75.right = bst80

# bst100.right = bst150
# bst150.left = bst140
# bst150.right = bst200


# ---------------------------------------------------------------------------

"""
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
bst11 = Node(11)

bst1.left = bst2
bst1.right = bst7

bst2.left = bst3

bst3.right = bst4

bst4.left = bst5
bst4.right = bst6

bst7.right = bst8

bst8.left = bst9

bst9.left = bst10
bst9.right = bst11



bst4 = Node(4)

bst6 = Node(6)
bst3 = Node(3)
bst2 = Node(2)

bst4.right = bst6
bst6.left = bst3
bst3.right = bst2

"""

bst1 = Node(1)
bst2 = Node(2)
bst3 = Node(3)
bst4 = Node(4)
bst5 = Node(5)
bst6 = Node(6)

bst9 = Node(9)
bst10 = Node(10)
bst11 = Node(10)

bst1.left = bst2
bst1.right = bst3

bst2.left = bst4
bst2.right = bst10

bst4.right = bst5

bst5.right = bst6

bst3.left = bst9
bst3.right = bst11










