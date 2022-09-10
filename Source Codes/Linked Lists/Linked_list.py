class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Linked_list:
    def __init__(self):
        self.head = None
        self.current = None
        
        
    def create_list(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.current = new_node
            
        else:
            self.current.next = new_node
            self.current = new_node
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print(None)
            
            
l1 = [1, 5, 10]
l2 = [0, 2, 3]

list1 = Linked_list()
list2 = Linked_list()


for i in l1:
    list1.create_list(i)
    
for i in l2:
    list2.create_list(i)
  
if __name__ == '__main__':
    list1.display()
    list2.display()
    
    
        