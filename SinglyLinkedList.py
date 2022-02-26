from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            if current_node.next == None:
                current_node.next = new_node
                break
            current_node = current_node.next

    def insert_at_position(self, data, position):
        new_node = Node(data)
        current_node = self.head
        c = 0
        while current_node.next != None:
            if c == position - 1:
                new_node.next = current_node.next
                current_node.next = new_node
                break
            c += 1
            current_node = current_node.next

    def delete_at_first(self):
        self.head = self.head.next

    def delete_at_last(self):
        current_node = self.head
        while current_node.next != None:
            if current_node.next.next == None:
                current_node.next = None
                break
            current_node = current_node.next

    def delete_at_position(self, position):
        current_node = self.head
        c = 0
        while current_node.next != None:
            if c == position - 1:
                current_node.next = current_node.next.next
                break
            c += 1
            current_node = current_node.next
        

    def print_data(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=', ')
            current_node = current_node.next

        print()


data = SinglyLinkedList()

for i in range(10):
    data.insert_at_first(i)
data.print_data()
data.insert_at_last("LAST")
data.print_data()
data.insert_at_position("Middle", 5)
data.print_data()
data.delete_at_first()
data.print_data()
data.delete_at_last()
data.print_data()
data.delete_at_position(10)
data.print_data()
