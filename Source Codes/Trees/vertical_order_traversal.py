from bst_hardcoded import bst1
from collections import defaultdict


def fun(root,q_dict):
    
    queue = [(root, 0, 0)]
    
    q_dict[0] = [{0 : [root.data]}]
    
    while len(queue) > 0:
        q = queue.pop(0)
        
        if q[0].left:
            d = q[1]-1
            l = q[2]+1
            queue.append((q[0].left, d, l))
            
            
            if q_dict[d] == None:
                q_dict[d] = [{l : [q[0].left.data]}]
            else:
                flag = False
                for i in range(len(q_dict[d])):
                    key, = q_dict[d][i]
                    if key == l:
                        q_dict[d][i][l].append(q[0].left.data)
                        q_dict[d][i][l].sort()
                        
                        flag = True
                
                if flag == False:
                    q_dict[d].append({l : [q[0].left.data]})
                    
        if q[0].right:
            d = q[1]+1
            l = q[2]+1
            queue.append((q[0].right, d, l))
            
            
            if q_dict[d] == None:
                q_dict[d] = [{l : [q[0].right.data]}]
            else:
                flag = False
                for i in range(len(q_dict[d])):
                    key, = q_dict[d][i]
                    if key == l:
                        flag = True
                        q_dict[d][i][l].append(q[0].right.data)
                        q_dict[d][i][l].sort()
                
                if flag == False:
                    q_dict[d].append({l : [q[0].right.data]})


def display(q_dict):
    key = sorted(q_dict)
    output = []
    for i in key:
        temp = []
        for j in q_dict[i]:
            for k, item in j.items():
                temp.extend(item)
        output.append(temp)
    
    return output


q_dict = defaultdict(lambda: None)
fun(bst1, q_dict)
output = display(q_dict)
print(output)




