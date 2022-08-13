from bst_hardcoded import bst1


def fun(node):
    if node == None:
        return 0
    
    left = 1 + fun(node.left)
    right = 1 + fun(node.right)
    
    if node.left == None or node.right == None:
        return max(left, right)
    
    return min(left, right)


out = fun(bst1)
print(out)