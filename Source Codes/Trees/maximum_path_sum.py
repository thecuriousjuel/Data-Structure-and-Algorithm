from bst_hardcoded import bst1

def fun(self, root, maxi):
    if root == None:
        return 0

    #print(root.val, maxi)

    left = max(0, self.fun(root.left, maxi))
    right = max(0, self.fun(root.right, maxi))

    maxi[0] = max(root.val+left+right, maxi[0])

    return root.val + max(left, right)


maxi = [float('-inf')]
out = fun(bst1, maxi)

print(maxi[0])

