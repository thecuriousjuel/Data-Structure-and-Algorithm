import LinkedList

def middle_elem(head):
    tortoise = head
    hare = head

    while hare != None and hare.next != None:
        tortoise = tortoise.next
        hare = hare.next.next

    return tortoise


output = middle_elem(LinkedList.ll.head)
print(output.data)
