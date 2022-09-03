# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    
    def fun(self, root, B, output):
        if root:
            output.append(root.val)
            
            if root.val == B:
                return True
            
            left = self.fun(root.left, B, output)
            right = self.fun(root.right, B, output)
            
            if left or right:
                return True
            
            output.pop()
        return False
            
    
    def solve(self, A, B):
        output = []
        
        self.fun(A, B, output)
        
        #print(output)
        return output
