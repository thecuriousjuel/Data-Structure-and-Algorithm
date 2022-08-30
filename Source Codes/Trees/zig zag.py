from bst_hardcoded import bst1

def level(root, out):
    queue = [[root]]
    out.append([root.data])
    count = 0
    
    while len(queue[0]) > 0:
        temp1 = []
        temp2 = []
        
        q = queue.pop(0)
        count += 1

        for i in q:
            if count % 2 == 0:
                if i.left:
                    temp1.append(i.left.data)
                    temp2.append(i.left)
                
                if i.right:
                    temp1.append(i.right.data)
                    temp2.append(i.right)
            else:
                if i.right:
                    temp1.append(i.right.data)
                    temp2.append(i.right)
                    
                if i.left:
                    temp1.append(i.left.data)
                    temp2.append(i.left)
                
        if temp1:
            out.append(temp1)
        queue.append(temp2[::-1])
        
        
       
out_list = []
level(bst1, out_list)
print(out_list)



