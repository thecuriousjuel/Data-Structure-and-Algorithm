from bst_hardcoded import bst1

def fun(bst1, llist):
    queue = [bst1]
    llist.append([bst1.data])
    
    while len(queue) > 0:
        
        temp = []
        l = len(queue)
        for i in range(l):
            
            if queue[i].left != None:
                queue.append(queue[i].left)
                temp.append(queue[i].left.data)
            
            if queue[i].right != None:
                queue.append(queue[i].right)
                temp.append(queue[i].right.data)
            
            
        if len(temp) > 0:
            llist.append(temp)
            
        queue = queue[l:]
        
        
        
llist = []
fun(bst1, llist)
print(llist)