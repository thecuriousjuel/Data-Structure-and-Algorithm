def fun(root, val):
    floor = -1
    
    while root:
        if root.data == val:
            return root.data
        
        elif root.data > val:
            root = root.left
        
        else:
            floor = root.data
            root = root.right
            
    return floor

def floorInBST(root, X):

    # Write your Code here.
    
    return fun(root, X)
