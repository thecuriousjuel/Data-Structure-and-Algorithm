class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def insert_at_position():
        pass

    def display(self):
        current = self.head
        while current != None:
            print(current.data, end=', ')
            current = current.next
        print()


d_list = DoublyLinkedList()
for i in range(10):
    d_list.insert_at_first(i)
d_list.display()
d_list.insert_at_end(20)
d_list.display()
