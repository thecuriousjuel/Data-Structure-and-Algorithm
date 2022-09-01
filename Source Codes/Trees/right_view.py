from bst_hardcoded import bst1


def fun(root):
    queue = [(root, 0, 0)]
    output = {}
    
    while queue:
        if root == None:
            return []
        
        node, d, l = queue.pop(0)
        
        output[l] = (d, node.data)
                
        if node.left:
            queue.append((node.left, d-1, l+1))
        
        if node.right:
            queue.append((node.right, d+1, l+1))
    
    final = []
    for i in output:
        final.append(output[i][1])
        
    return final
        
    
    
out = fun(bst1)
print(out)


