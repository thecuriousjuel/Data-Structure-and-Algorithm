from BinarySearchTree import bst

def height(root):
    if root != None:
        return max(height(root.left), height(root.right)) + 1
    else:
        return 0

print(height(bst.root))


