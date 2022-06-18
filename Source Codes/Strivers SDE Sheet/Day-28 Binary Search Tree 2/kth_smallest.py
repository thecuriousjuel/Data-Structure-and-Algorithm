from BinarySearchTree import bst


def kth_smallest(root, k, count=[0]):
    if root != None:
        left = kth_smallest(root.left, k, count)
        if left != None:
            return left
        
        count[0] += 1
        
        if count[0] == k:
            return root.data
        
        right = kth_smallest(root.right, k, count)
        if right != None:
            return right
    
print(kth_smallest(bst.root, k=1))