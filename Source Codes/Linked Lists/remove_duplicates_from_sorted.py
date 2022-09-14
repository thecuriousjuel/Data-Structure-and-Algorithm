# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def fun(self, head):
        
        # store the starting node
        current = head
        
        while current:
            if current.next:
                
                # if the current node's and next node's value is matching
                # then point current node to the next to next node(can be null),
                # the intermediate node link gets removed.
                if current.val == current.next.val:
                    current.next = current.next.next
                    
                # if the current node and the next node is not matching
                # just shift the current node to the next node
                else:
                    current = current.next
            else:
                break
        
        return head
                   
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.fun(head)
        