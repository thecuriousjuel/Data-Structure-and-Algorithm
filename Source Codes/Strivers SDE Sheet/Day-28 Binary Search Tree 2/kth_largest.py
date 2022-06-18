from BinarySearchTree import bst


def kth_largest(root, k, count=[0]):
    if root != None:
        left = kth_largest(root.right, k, count)
        if left != None:
            return left
        
        count[0] += 1
        
        if count[0] == k:
            return root.data
        
        right = kth_largest(root.left, k, count)
        if right != None:
            return right
    
print(kth_largest(bst.root, k=1))
