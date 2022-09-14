# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                
    def fun(self, root, min_range, max_range):  
        
        # checking for leaf condition
        if root == None:
            return True
        
        # if the current node value satisfies bst condition
        if min_range >= root.val or max_range <= root.val:
            return False
        
        left = self.fun(root.left, min_range, root.val)
        right = self.fun(root.right, root.val, max_range)
            
        return left and right
        
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # start with the -inf and +inf as min and max value respectively
        return self.fun(root, min_range=float('-inf'), max_range=float('inf'))
        