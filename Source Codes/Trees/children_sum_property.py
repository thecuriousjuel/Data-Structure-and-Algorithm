from bst_hardcoded import bst1

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)
        

def fun(root):
    if root:
        left = 0
        if root.left:
            left = root.left.data
            
        right = 0
        if root.right:
            right = root.right.data
            
        if left + right < root.data:            
            if root.left:
                root.left.data = root.data
            
            if root.right:
                root.right.data = root.data
        
        
        fun(root.left)
  
        fun(root.right)
            
        left = 0
        if root.left:
            left = root.left.data
            
        right = 0
        if root.right:
            right = root.right.data
            
        if left+right >= root.data:
            root.data = left + right
        
preorder(bst1)
print()

fun(bst1)

preorder(bst1)
                  
 