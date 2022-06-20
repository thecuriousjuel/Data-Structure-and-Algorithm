from BinarySearchTree import bst


def right_view(root, level=0, out=[]):
    if root != None:
        if level == len(out):
            out.append(root.data)
            
        right_view(root.right, level+1, out)
        right_view(root.left, level+1, out)

    if level == 0:
        print(out)

right_view(bst.root)
