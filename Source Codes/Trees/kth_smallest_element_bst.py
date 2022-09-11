# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def fun(self, root):
        if root:
            # if the left subtree returns a value, do return the value back
            l = self.fun(root.left)
            if l != None:
                return l
            
            # decrease the value of k
            self.k -= 1
            
            # if k reaches on the required node, the value will be zero
            # checking for the zero condition and returning the current node value
            if self.k == 0:
                return root.val
            
            # if the right subtree returns a value, do return the value back
            r = self.fun(root.right)
            if r != None:
                return r

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Pass k via reference
        self.k = k
        
        out = self.fun(root)        
        return out
        