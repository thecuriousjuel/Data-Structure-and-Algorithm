import LinkedList


def check_palindromic(head):
    current = head
    string1 = ''
    string2 = ''

    while current != None:
        string1 = string1 + str(current.data)
        string2 = str(current.data) + string2
        current = current.next

    if string1 == string2:
        return 'Palindrome'
    return 'Not Palindrome'


print(check_palindromic(LinkedList.ll.head))