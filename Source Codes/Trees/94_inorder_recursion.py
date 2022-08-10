# TC - O(N) SC-O(N)

class Solution:
    def fun(self, root, llist):
        if root != None:
            self.fun(root.left, llist)
            llist.append(root.val)
            self.fun(root.right, llist)
            
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        llist = []
        self.fun(root, llist)
        return llist