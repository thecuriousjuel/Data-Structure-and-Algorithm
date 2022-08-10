# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, root, llist):
        if root != None:
            llist.append(root.val)
            self.fun(root.left, llist)
            self.fun(root.right, llist)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        llist = []
        self.fun(root, llist)
        return llist
    
    
# TC - O(N)
# SC - O(N)