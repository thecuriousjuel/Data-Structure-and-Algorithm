from BinarySearchTree import bst


def left_view(root, level=0, out=[]):
    if root != None:
        if level == len(out):
            out.append(root.data)
            
        left_view(root.left, level+1, out)
        left_view(root.right, level+1, out)
        
    if level == 0:
        print(out)


left_view(bst.root)


