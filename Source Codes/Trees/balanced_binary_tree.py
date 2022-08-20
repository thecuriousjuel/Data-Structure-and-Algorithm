from bst_hardcoded import bst1


def fun(root):
    if root == None:
        return 0
    
    left = fun(root.left)
    right = fun(root.right)
    
    bf = abs(left - right)
    if bf > 1:
        return float('inf')
    
    return max(left, right) + 1



out = fun(bst1)
if out == float('inf'):
    print('False')
else:
    print('True')
    
    
    