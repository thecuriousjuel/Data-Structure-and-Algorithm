import LinkedList

def detect_cycle(head):
    slow = head
    fast = head.next

    flag = 0

    while True:
        if slow is fast:
            flag = 1
            break

        slow = slow.next

        if fast.next == None or fast.next.next == None:
            break
        fast = fast.next.next

    if flag == 1:
        print('Cycle exists')
    else:
        print('Cycle doesnot exists')


current = LinkedList.ll.head

while current.next != None:
    current = current.next

current.next = LinkedList.ll.head


detect_cycle(LinkedList.ll.head)