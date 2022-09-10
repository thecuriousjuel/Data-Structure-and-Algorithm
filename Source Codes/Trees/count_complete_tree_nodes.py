# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def left_height(self, root):
        if root == None:
            return 0

        return 1 + self.left_height(root.left)


    def right_height(self, root):
        if root == None:
            return 0

        return 1 + self.right_height(root.right)


    def fun(self, root): 

        lh = self.left_height(root)
        rh = self.right_height(root)

        if lh != rh:
            l = self.fun(root.left)
            r = self.fun(root.right)

            return l + r + 1
        else:
            return (2 ** lh) - 1
        
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        out = self.fun(root)
        return out
        