# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def fun(self, root, temp, out):
        if root:
            # checking for leaf condition
            if root.left == None and root.right == None:
                temp.append(root.val)
                out.append(temp[:])
                temp.pop()
                return 
                
            # checking for left subtree
            temp.append(root.val)
            self.fun(root.left, temp, out)

            # checking for right subtree
            self.fun(root.right, temp, out)
            temp.pop()
   

    def display(self, l):
        # function to add '->' in between
        t = ''
        for i in l:
            t += str(i) + '->'

        return t[:-2]
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # calling function (starting point)
        temp = []
        out = []
        
        self.fun(root, temp, out)
        
        temp = []
        for i in out:
            temp.append(self.display(i))
            
        return temp
        
        
        