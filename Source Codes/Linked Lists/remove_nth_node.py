import LinkedList

def remove_nth(head, n):
    current = head
    while current != None:
        print(current.data, end = ' ')
        current = current.next
    print()

    current = head
    count = 0

    while current != None:
        count += 1
        current = current.next

    index = 0
    delete_node_index = count - n
    current = head

    if delete_node_index == 0:
        head = current.next
    else:
        while current != None:
            if index + 1 == delete_node_index:
                current.next = current.next.next

            index += 1
            current = current.next

    current = head
    while current != None:
        print(current.data, end = ' ')
        current = current.next
    print()



remove_nth(LinkedList.ll.head, n = 1)







