# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, head, val):
        # store the head node on root
        root = head
        
        while root:
            
            if val > root.val:
                # if there is right sub tree, go to right subtree
                if root.right:
                    root = root.right
                    
                # else create the node and assign to the root's right
                else:
                    root.right = TreeNode(val)
                    break
                
            elif val < root.val:
                # if there is left sub tree, go to left subtree
                if root.left:
                    root = root.left
                    
                # else create the node and assign to the root's left
                else:
                    root.left = TreeNode(val)
                    break
                    
        return head
    
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If root is initially empty, create the root node
        if root == None:
            return TreeNode(val)
        
        # If the root node is not empty
        return self.fun(root, val)
        