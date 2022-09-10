# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, head):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if head == None:
            return ''
        
        queue = [head]
        ans = str(head.val) + ','

        while queue:
            d = queue.pop(0)

            if d.left:
                queue.append(d.left)
                ans += str(d.left.val) + ','
            else:
                ans += '#,'

            if d.right:
                queue.append(d.right)
                ans += str(d.right.val) + ','
            else:
                ans += '#,'

        return ans[:-1]
        
    
    def deserialize(self, s):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if len(s) == 0:
            return None
        
        s = s.split(',')

        ind = 0
        head = TreeNode(s[ind])

        queue = [head]

        while ind < len(s) and queue:
            d = queue.pop(0)

            ind += 1

            if s[ind] != '#':
                left = TreeNode(s[ind])
                d.left = left
                queue.append(left)
            else:
                d.left = None

            ind += 1

            if s[ind] != '#':
                right = TreeNode(s[ind])
                d.right = right
                queue.append(right)
            else:
                d.right = None

        return head
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))