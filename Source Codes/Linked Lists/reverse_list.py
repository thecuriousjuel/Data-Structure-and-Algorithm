from LinkedList import ll 

def reverse(head):
    past = None
    present = head
    future = head
    
    while future != None:
        future = future.next
        present.next = past
        past = present
        present = future
        
    return past
        
        
        
new_head = reverse(ll.head)
while new_head:
    print(new_head.data, end='\t')
    new_head = new_head.next
    
    