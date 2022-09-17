from hardcoded_binary_tree import *


def fun(root):
    if root == None:
        return 0, float('-inf'), float('inf')
    
    l_tree = fun(root.left)
    r_tree = fun(root.right)
    
    print(root.data, l_tree, r_tree)
    
    if l_tree[1] < root.data < r_tree[2]:
        
        count = 1 + l_tree[0] + r_tree[0]
        lar = max(l_tree[1], r_tree[1], root.data)
        sma = min(l_tree[2], r_tree[2], root.data)
        
    else:
        count = max(l_tree[0], r_tree[0])
        lar = float('inf')
        sma = float('-inf')
        
    return count, lar, sma


print('Node \t Left \t\t Right')
out = fun(bt20)
print(out)


