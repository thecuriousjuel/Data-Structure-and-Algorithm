from bst_hardcoded import bst1

def fun(root, llist):
    stack = []
    node = root
    
    while True:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            
            node = stack[-1]
            stack.pop()
            llist.append(node.data)
            node = node.right
            

llist = []
if bst1 != None:
    out = fun(bst1, llist)
print(llist)

