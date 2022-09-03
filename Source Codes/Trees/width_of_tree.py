from bst_hardcoded import bst1

    
def display(llist):
    temp = []
    for i in llist:
        if i:
            temp.append(i.data)
        else:
            temp.append(None)
    # print(temp)
    return temp

    
def fun(root):

    queue = [root]
    max_width = float('-inf')
    output = []
    
    while queue:
        result = display(queue)
        output.append(result)
        
        size = len(queue)
        max_width = max(max_width, size)
        temp = []
        flag = False
        
        for i in range(size):
            node = queue.pop(0)
            if node == None:
                continue
            
            if node.left or node.right:
                flag = True
                
            temp.append(node.left)
            temp.append(node.right)
        
        if flag:
            queue.extend(temp) 
                
    return output
 

out = fun(bst1)
#print(out)



max_width = float('-inf')

for i in out:
    start = None
    stop = None
    
    for j in range(len(i)):
        if i[j] != None and start == None:
            start = j
        
        if i[len(i)-1-j] != None and stop == None:
            stop = len(i)-1-j
    
    #print(i[start:stop+1], start,stop)
    #print(max_width, len(i[start:stop+1]))
    max_width = max(max_width, len(i[start:stop+1]))
            
print(max_width)
        
            
            
        
            
















