import Binary_Search_Tree


def inorder(current):
    if current != None:
        inorder(current.left)
        print(current.data, end = ' ')
        inorder(current.right)


inorder(Binary_Search_Tree.bst.root)
print()