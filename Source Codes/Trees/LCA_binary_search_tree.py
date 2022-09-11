# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def fun(self, root, n1, n2):
        
        while root:
            lca = root.val
            
            # If both the starting and ending nodes are less 
            # than root then shift to left side
            if n1 < lca and n2 < lca:
                root = root.left
            
            # If both the starting and ending nodes are greater 
            # than root then shift to right side
            elif n1 > lca and n2 > lca:
                root = root.right
            
            # If both the starting and ending nodes have a common
            # ancestor when one node lies at left and the other lies
            # at the right side then return the common root node
            else:
                return TreeNode(lca)
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.fun(root, p.val, q.val)
        