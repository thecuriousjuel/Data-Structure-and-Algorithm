import Binary_Search_Tree


def kth_largest(root, k, arr = []):
    if len(arr) == k:
        return arr[-1]

    if root != None:
        right = kth_largest(root.right, k, arr)
        if right != None:
            return right

        arr.append(root.data)
        
        left = kth_largest(root.left, k, arr)
        if left != None:
            return left


root = Binary_Search_Tree.bst.root
k = 3
print(kth_largest(root, k))



