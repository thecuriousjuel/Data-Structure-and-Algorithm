import Binary_Search_Tree

def postOrder(current):
    if current != None:
        postOrder(current.left)
        postOrder(current.right)
        print(current.data, end=' ')


postOrder(Binary_Search_Tree.bst.root)
print()