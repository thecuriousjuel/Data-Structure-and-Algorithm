import Binary_Search_Tree


def kth_smallest(root, k, arr = []):
    if len(arr) == k:
        return arr[-1]

    if root != None:
        left = kth_smallest(root.left, k, arr)
        if left != None:
            return left

        arr.append(root.data)
        
        right = kth_smallest(root.right, k, arr)
        if right != None:
            return right

    


root = Binary_Search_Tree.bst.root
k = 3
print(kth_smallest(root, k))



