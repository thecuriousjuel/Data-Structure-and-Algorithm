import Binary_Search_Tree


def height(root):
    if root != None:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1
 
    return 0



print(height(Binary_Search_Tree.bst.root))