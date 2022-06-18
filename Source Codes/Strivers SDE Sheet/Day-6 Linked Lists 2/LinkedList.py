class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def add_node_helper(self, new_node):
        current = self.head
        while current.next != None:
            current = current.next
            
        current.next = new_node
        
        
        
    def add_node(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            
        else:
            self.add_node_helper(new_node)
            
            
    def display(self):
        current = self.head
        
        
        while current != None:
            print(current.data, end = ' ')
            current = current.next
            
            
my_list = LinkedList()
# my_list.add_node(1)
# my_list.add_node(2)
# my_list.add_node(3)
# my_list.add_node(3)
# my_list.add_node(2)
# my_list.add_node(1)
# my_list.add_node(6)

print('-----------Original List-----------')
my_list.display()
print('\n-----------------------------------')
