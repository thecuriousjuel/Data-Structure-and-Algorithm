from bst_hardcoded import bst3

def fun(root, p, q):
    if root:
    
        if root.data == p or root.data == q:
            return root.data
        
        left = fun(root.left, p, q)
        right = fun(root.right, p, q)
        
        if left and right:
            return root.data
        
        return left or right


out = fun(bst3, 5, 1)

print(out)
        



