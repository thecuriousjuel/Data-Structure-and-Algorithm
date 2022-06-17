from LinkedList import my_list
import LinkedList

def remove_nth(head, N):
    current = head
    count = 0
    
    while current != None:
        count += 1
        current = current.next
        
        
    N_index = count - N - 1
    if N_index < 0:
        return None
    
    count = 0
    
    current = head
    
    while current != None:
        if count == N_index:
            current.next = current.next.next
            
        count += 1
        current = current.next
        
    return head


n = 5
new_head = remove_nth(my_list.head, n)

while new_head != None:
    print(new_head.data, end=' ')
    new_head = new_head.next
print()















