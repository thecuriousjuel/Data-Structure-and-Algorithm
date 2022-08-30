from bst_hardcoded import bst1

def preorder(root, out):
    if root:
        out.append(root.data)
        preorder(root.left, out)
        preorder(root.right, out)
    
    
def postorder(root, out):
    if root:
        postorder(root.left, out)
        postorder(root.right, out)
        out.append(root.data)
        

def fun(root, out):
    out.append(root.data)
    
    if root.left:
        preorder(root.left, out)
    
    if root.right:
        postorder(root.right, out)


out = []
fun(bst1, out)
print(out)


