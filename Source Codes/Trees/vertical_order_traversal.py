from bst_hardcoded import bst1
from collections import defaultdict


def fun(root, q_dict):
    
    queue = [(root, 0, 0)]
    
    while queue:
        size = len(queue)
        
        for _ in range(size):
        
            node, d, l = queue.pop(0)
            q_dict[d].append((l, node.data))                      
        
            if node.left:
                queue.append((node.left, d-1, l+1))

            if node.right:
                queue.append((node.right, d+1, l+1))


def display(q_dict):
    print(q_dict)
    output = []
    
    for i in sorted(q_dict):
        temp = []
        for j in sorted(q_dict[i]):
            temp.append(j[1])
        output.append(temp)
    
    
    return output


q_dict = defaultdict(list)
fun(bst1, q_dict)

output = display(q_dict)
print(output)




