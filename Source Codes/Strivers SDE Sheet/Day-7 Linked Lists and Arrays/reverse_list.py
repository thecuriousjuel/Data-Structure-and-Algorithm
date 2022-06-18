from LinkedList import my_list

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
        
        
        
new_head = reverse(my_list.head)
while new_head:
    print(new_head.data, end=' ')
    new_head = new_head.next
    
    