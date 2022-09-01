from bst_hardcoded import bst1


def fun(root):
    queue = [root]
    output = [[root.data]]
    
    while queue:
        size = len(queue)
        temp = []
        
        for i in range(size):
            q = queue.pop(0)
            
            if q.left:
                queue.append(q.left)
                temp.append(q.left.data)
                
            if q.right:
                queue.append(q.right)
                temp.append(q.right.data)
        
        if temp:
            output.append(temp)
            if len(temp) % 2 != 0:
                return False
            
            size = len(temp)
            for i in range(size // 2):
                if temp[i] == temp[size-i-1]:
                    continue
                else:
                    return False
    print(output)
    
    return True
          
              
out = fun(bst1)
print(out)


