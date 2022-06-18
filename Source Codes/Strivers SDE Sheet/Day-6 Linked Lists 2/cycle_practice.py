from LinkedList import my_list

def cycle(head):
    if head == None:
        print('No Cycle present')
        return
    
    slow = head
    fast = head.next
    flag = 0
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            flag = 1
            break
        
    if flag == 1:
        print('Cycle present')
    else:
        print('No Cycle present')
        
    
        
        
# creating a cycle
# current = my_list.head
# while current.next != None:
#     current = current.next
#     
# current.next = my_list.head

# checking cycle
# current = my_list.head
# count = 0
# while current.next != None:
#     if count == 20:
#         break
#     print(current.data, end = ' ')
#     current = current.next
#     count += 1
    
print()
cycle(my_list.head)

