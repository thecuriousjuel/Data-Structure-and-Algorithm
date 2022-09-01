from bst_hardcoded import bst1


def fun(root):
    queue = [(root, 0, 0)]

    output = {}
    l = None
    
    while queue:
        
        node, d, l = queue.pop(0)
        
        l = node.data
        
        if node.right:
            queue.append((node.right, d+1, l+1))
    
        if node.left:
            queue.append((node.left, d-1, l+1))
    
    return l
            
            
out = fun(bst1)
print(out)
            