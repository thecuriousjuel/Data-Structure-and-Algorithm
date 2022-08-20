class Solution:
    
    def fun(self, root):
    
        if root == None:
            return 0

        left = self.fun(root.left)
        right = self.fun(root.right)

        self.maxi = max(self.maxi, left+right)

        return max(left, right) + 1

    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = float('-inf')
        self.fun(root)

        return self.maxi