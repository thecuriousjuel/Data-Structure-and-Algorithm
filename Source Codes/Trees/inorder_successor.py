from hardcoded_binary_tree import *


def fun(root, value):
    parent = None
    
    while root:
        if value >= root.val:
            root = root.right
        else:
            parent = root
            root = root.left
            
    return parent


for i in [5, 6, 7, 8]:
    
    out = fun(bst5, i)
    print('Input : ', i)
    if out:
        print('Output : ', out.val)
    else:
        print('Output : ', out)


