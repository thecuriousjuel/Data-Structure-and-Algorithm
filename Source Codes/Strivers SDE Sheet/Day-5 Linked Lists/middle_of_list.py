from LinkedList import my_list

def middle(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    while slow != None:    
        print(slow.data, end=' ')
        slow = slow.next
    
    
middle(my_list.head)

