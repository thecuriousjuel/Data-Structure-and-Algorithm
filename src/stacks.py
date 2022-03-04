class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stacks:
    def __init__(self):
        self.head = None

    def push(self, data):

        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
 
        self.head = new_node

    def pop(self):
        if self.head is None:
            print('Stack is Empty')
        else:
            self.head = self.head.next

    def display(self):
        current = self.head

        while current:
            print(current.data, end = ' ')
            current = current.next
        print()
        


stack = Stacks()
try:
    while True:
        print('1. Push Element')
        print('2. Pop Element')
        n = eval(input('->'))

        if n == 1:
            data = eval(input('Enter data ->'))
            stack.push(data)

        elif n == 2:
            stack.pop()
        
        
        stack.display()
    
except KeyboardInterrupt:
    print('Exiting...')

