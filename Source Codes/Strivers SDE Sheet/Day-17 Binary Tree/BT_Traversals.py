from BinarySearchTree import bst

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end = '\t')
        inorder(root.right)
        
        
def preorder(root):
    if root != None:
        print(root.data, end='\t')
        preorder(root.left)
        preorder(root.right)
        
        
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='\t')
        

print('Inorder : ', end='')
inorder(bst.root)
print()

print('Preorder : ', end='')
preorder(bst.root)
print()

print('Postorder : ', end='')
postorder(bst.root)
print()

