# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Function to check for the leaf condition
    def is_leaf(self, node):
        if node.left == None and node.right == None:
            return True
        return False
    
    
    def fun(self, root, t):
        if root:
            
            # checking for the leaf condition
            if self.is_leaf(root):
                return t-root.val == 0
            
            l = self.fun(root.left, t-root.val)
            if l:
                return l
            
            r = self.fun(root.right, t-root.val)
            if r:
                return r
            
            # return l or r
        
        return False
            
            
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.fun(root, targetSum)
        