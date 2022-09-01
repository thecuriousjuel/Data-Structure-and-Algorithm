# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, root, value):
        if root:
            # checking for matching values, if not return false
            if root.val != value:
                return False
            
            left = self.fun(root.left, value)
            right = self.fun(root.right, value)
            
            # if false received on any side perform an and operation 
            # resulting to return false ultimately
            
            return left and right
        return True
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.fun(root, root.val)