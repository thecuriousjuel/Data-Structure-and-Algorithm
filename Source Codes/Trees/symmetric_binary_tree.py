# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def fun(self, l_root, r_root):
        
        # if nodes are not matching. Eg- one node contains value and the other is None
        if l_root == None or r_root == None:
            return l_root == r_root
            
        # Checking for value match
        if l_root.val != r_root.val:
            return False
        
        # Left Tree- Left Traversal, Right Tree- Right Traversal
        left = self.fun(l_root.left, r_root.right)
        
        # Left Tree- Right Traversal, Right Tree- Left Traversal
        right = self.fun(l_root.right, r_root.left)

        # Returning True if both the trees and subtrees are identical 
        return left and right
    

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Calling method
        return self.fun(root, root)
        
        
        
        