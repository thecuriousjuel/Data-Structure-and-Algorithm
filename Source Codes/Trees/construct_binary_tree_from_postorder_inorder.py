# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, inorder, i_start, i_end, postorder, p_start, p_end, d):
        
        # This is the leaf condition.
        # If the element has no left or right elements present.
        if i_start > i_end or p_start > p_end:
            return None
        
        # create the root node for the tree/subtree
        root = TreeNode(postorder[p_end])
        
        # get the index from the inorder index dictionary
        i_index = d[root.val]
        
        # find the no. of elements on the left and right
        elems_on_left = i_index - i_start
        elems_on_right = i_end - i_index

        # Send the starting and ending indexes of the 
        # inorder and  preorder array 
        root.left = self.fun(inorder, i_start, i_start + elems_on_left - 1,
                        postorder, p_start, p_start + elems_on_left - 1, d)

        root.right = self.fun(inorder, i_index + 1, i_end,
                         postorder, p_end - elems_on_right, p_end-1, d)

        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # Create a dictionary to store inorder index details
        d = {}

        for i in range(len(inorder)):
            d[inorder[i]] = i

        i_start = 0
        i_end = len(inorder)-1

        p_start = 0
        p_end = len(postorder)-1

        out = self.fun(inorder, i_start, i_end,
                  postorder, p_start, p_end, d)
        
        return out