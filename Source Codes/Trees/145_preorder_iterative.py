from bst_hardcoded import bst1

def fun(root, llist):
    stack = [root]
    
    while len(stack) > 0:
        d = stack.pop()
        
        llist.append(d.data)
        
        if d.right:
            stack.append(d.right)
            
        if d.left:
            stack.append(d.left)
            
        
llist = []
if bst1 != None:
    out = fun(bst1, llist)
print(llist)
