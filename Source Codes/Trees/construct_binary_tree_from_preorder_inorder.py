# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, preorder, pre_start, pre_end, inorder, in_start, in_end, d):
    
        if pre_start > pre_end or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])

        in_root = d[preorder[pre_start]]
        nums_left = in_root - in_start

        root.left = self.fun(preorder, pre_start + 1, pre_start + nums_left,
                        inorder, in_start, in_root - 1, d)

        root.right = self.fun(preorder, pre_start + nums_left + 1, pre_end,
                         inorder, in_root + 1, in_end, d)

        return root
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        d = {}

        for i in range(len(inorder)):
            d[inorder[i]] = i

        out = self.fun(preorder = preorder,
            pre_start = 0,
            pre_end = len(preorder) - 1,
            inorder = inorder,
            in_start = 0,
            in_end = len(inorder) - 1,
            d = d)

        return out
        