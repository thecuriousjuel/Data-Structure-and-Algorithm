# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def fun(self, root, l):
        # Do an inorder traversal and 
        # store all the tree nodes on a list.
        if root:
            self.fun(root.left, l)
            
            # Store only the unique elements
            if root.val not in l:
                l.append(root.val)
            self.fun(root.right, l)
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l = []
        
        self.fun(root, l)
        
        # If the list is empty or doesnot have more than 
        # 1 unique value return -1 else sort the list
        # and return the 1st element (Zero based indexing)
        if len(l) <= 1:
            return -1
        return sorted(l)[1]
        
        