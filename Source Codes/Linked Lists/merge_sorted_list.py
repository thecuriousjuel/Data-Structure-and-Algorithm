from Linked_list import *

node1, node2 = list1.head, list2.head

while node1 and node2:
    print('-' * 50)
    
    list1.display()
    print(f'Current Node {node1.data}')
    
    list2.display()
    print(f'Current Node {node2.data}')
    
    if node1.data <= node2.data:
        if not node1.next:
            node1.next = node2
            break
            
        elif node1.next.data < node2.data:
            node1 = node1.next
        
        else:
            temp1 = node1.next
            temp2 = node2.next
            
            node1.next = node2
            node2.next = temp1
            
            node2 = temp2
            node1 = node1.next
            
    else:
        node1.data, node2.data = node2.data, node1.data
        






