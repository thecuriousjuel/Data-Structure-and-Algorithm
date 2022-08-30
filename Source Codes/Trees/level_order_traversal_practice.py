from bst_hardcoded import bst1

def level(root, out):
    queue = [[root]]
    out.append([root.data])
    
    while len(queue[0]) > 0:
        temp1 = []
        temp2 = []
        
        q = queue.pop(0)

        for i in q:
            if i.left:
                temp1.append(i.left.data)
                temp2.append(i.left)
            
            if i.right:
                temp1.append(i.right.data)
                temp2.append(i.right)
                
        if temp1:
            out.append(temp1)
        queue.append(temp2)
        
       
out_list = []
level(bst1, out_list)
print(out_list)


