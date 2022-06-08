import LinkedList


def middle(head):
    current = head
    count = 0

    while current != None:
        count += 1
        current = current.next

    mid_value = count // 2
    index = 0
    current = head

    while current !=  None:
        if index == mid_value:
            print(current.data)
        index += 1
        current = current.next


middle(LinkedList.ll.head)
