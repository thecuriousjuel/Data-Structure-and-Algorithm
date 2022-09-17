from hardcoded_binary_tree import *


def fun(root, value):
    parent = None
    
    while root:
        if value > root.val:
            parent = root
            root = root.right
        else:
            root = root.left
            
    return parent


for i in range(1, 11):
    
    out = fun(bst5, i)
    print('Input : ', i)
    if out:
        print('Output : ', out.val)
    else:
        print('Output : ', out)



