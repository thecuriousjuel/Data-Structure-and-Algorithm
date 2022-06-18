from LinkedList import my_list

def rotate(head, k):
    if head == None:
        return 'Empty List'
    
    if head.next == None:
        return head
    
    for i in range(k):
        current = head
        
        while current.next.next != None:
            current = current.next
            
        temp = current.next
        current.next = None
        temp.next = head
        head = temp
        
    return head
        
new_head = rotate(my_list.head, k=4)
while new_head:
    print(new_head.data, end=' ')
    new_head = new_head.next
    
print()
