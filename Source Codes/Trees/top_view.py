from bst_hardcoded import bst1


def fun(root):
    if root == None:
        return []
    
    queue = [(root, 0)]
    output = {}
    
    while queue:
        
        node, d = queue.pop(0)
            
        if d not in output.keys():
            output[d] = node.data
            
        if node.left:
            queue.append((node.left, d-1))
        
        if node.right:
            queue.append((node.right, d+1))
        
    temp = []
    for i in sorted(output):
        temp.append(output[i])
        
    return temp
    
    
 
output = fun(bst1)
print(output)



        