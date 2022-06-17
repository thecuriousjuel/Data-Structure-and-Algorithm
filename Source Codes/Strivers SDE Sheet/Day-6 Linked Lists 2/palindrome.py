import LinkedList

def palindrome(head):
    current = head
    p1 = ''
    p2 = ''
    
    while current != None:
        p1 = p1 + str(current.data)
        p2 = str(current.data) + p2
        
        current = current.next
        
    if p1 == p2:
        return True
    
    return False


print(palindrome(LinkedList.my_list.head))
