class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, val):
        new_node = Node(val)

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
            print(current.val, end = '  ')
            current = current.next

        print()


arr = [1,1,2,2,3]

l = LinkedList()

for i in arr:
    l.add(i)

if __name__ == '__main__':
    l.display()

