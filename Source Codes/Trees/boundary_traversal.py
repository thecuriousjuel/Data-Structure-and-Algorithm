from bst_hardcoded import *

def is_leaf(root):
    if root.left == None and root.right == None:
        return True
    return False


def left_traversal(root, out):
    if root != None and not is_leaf(root):
        out.append(root.data)
        
        if root.left:
            left_traversal(root.left, out)
            
        elif root.right:
            left_traversal(root.right, out)
            

def right_traversal(root, temp):
    if root != None and not is_leaf(root):
        temp.append(root.data)
        
        if root.right:
            right_traversal(root.right, temp)
        elif root.left:
            right_traversal(root.left, temp)
        
        
def leaf_traversal(root, out):
    if root:
        leaf_traversal(root.left, out)
        
        if is_leaf(root):
            out.append(root.data)
            
        leaf_traversal(root.right, out)
            
        
def fun(root, out):

    out.append(root.data)
    
    if root:
        left_traversal(root.left, out)
    
    if not is_leaf(root):
        leaf_traversal(root, out)
    
    temp = []
    if root.right:
        right_traversal(root.right, temp)
        
    out.extend(temp[::-1])


out = []
fun(bst4, out)
print(out)


