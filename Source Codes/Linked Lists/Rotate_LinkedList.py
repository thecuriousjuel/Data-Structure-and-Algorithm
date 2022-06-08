import LinkedList


def rotate(head, n):
    for _ in range(n):
        current = head

        while current.next != None:
            current = current.next

        temp = current
        current = head

        # print(temp.data, current.data)

        while current.next != None:
            if current.next is temp:
                data = current.next
                current.next = None
                break

            current = current.next

        data.next = head
        head = data

    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


rotate(LinkedList.ll.head, 200)
