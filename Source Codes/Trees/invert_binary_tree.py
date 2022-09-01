# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, root):
        if root == None:
            return root
        
        queue = [root]
        
        while queue:
            
            node = queue.pop(0)
            
            node.left, node.right = node.right, node.left
            
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)

        return root
 
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        out = self.fun(root)
        return out
        
        