import Binary_Search_Tree

def preOrder(current):
    if current != None:
        print(current.data, end= ' ')
        preOrder(current.left)
        preOrder(current.right)



preOrder(Binary_Search_Tree.bst.root)
print()