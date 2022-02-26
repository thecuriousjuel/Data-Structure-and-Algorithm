class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node
        else:
            self.head = new_node

    def insert(self, data, position):
        temp = self.head
        count = 0

        new_node = Node(data)

        while temp:
            if position-1 == count:
                new_node.next = temp.next
                temp.next = new_node
                return
                
            count += 1
            temp = temp.next
    
    def get_position(self, data):
        temp = self.head
        count = 0
        while temp:
            if temp.data == data:
                return 'Found at : ' +  str(count)
                
            count += 1
            temp = temp.next

        return 'Not Found'
        
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
            
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            
            current = current.next

    def display(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next


mylist = LinkedList()
for i in range(4):
    n = eval(input('Enter a value -> '))
    mylist.append(n)

for i in mylist.display():
    print(i, end = ', ')
print()

# n = eval(input('Enter a number to Find -> '))
# print(mylist.get_position(n))

# mylist.insert(eval(input('Enter a number to insert -> ')), eval(input('Enter a position to insert -> ')))

# for i in mylist.display():
#     print(i, end = ', ')
# print()

mylist.delete(eval(input('Enter a number to delete -> ')))

for i in mylist.display():
    print(i, end = ', ')
print()
