'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def fun(root, val):
    ceil_val = -1
    
    while root:
        if root.data == val:
            ceil_val = root.data
            return ceil_val
        
        if root.data < val:
            root = root.right
        else:
            ceil_val = root.data
            root = root.left
           
    return ceil_val

            
def findCeil(root, x):
    # Write your code here.

    return fun(root, x)

    