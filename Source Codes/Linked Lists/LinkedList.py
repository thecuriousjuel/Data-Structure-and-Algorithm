class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next != None:
                current = current.next
            
            current.next = new_node


    def display(self):
        current = self.head

        while current != None:
            print(current.data, end = '\t')
            current = current.next

        print()



arr = [3,6,8,10]
ll = LinkedList()

for i in arr:
    ll.add(i)

# ll.display()

