class Solution:
    def fun(self, root, llist):
        if root != None:
            self.fun(root.left, llist)
            self.fun(root.right, llist)
            llist.append(root.val)
        
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        llist = []
        self.fun(root, llist)
        return llist
    
    
# TC - O(N) SC - O(N)