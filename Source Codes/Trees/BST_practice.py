class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert_helper(self, root, new_node):
        if new_node.data < root.data:
            if root.left == None:
                root.left = new_node
            else:
                self.insert_helper(root.left, new_node)

        else:
            if root.right == None:
                root.right = new_node
            else:
                self.insert_helper(root.right, new_node)


    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            self.insert_helper(self.root, new_node)

    
    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.data, end = ' ')
            self.inorder(root.right)


    def preorder(self, root):
        if root != None:
            print(root.data, end = ' ')
            self.preorder(root.left)
            self.preorder(root.right)

    
    def postorder(self, root):
        if root != None: 
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end = ' ')


    def search_iter(self, root, search_item):
        flag = 0

        while root:
            print(root.data)
            if search_item < root.data:
                root = root.left
            elif search_item > root.data:
                root = root.right
            else:
                flag = 1
                break

        if flag == 1:
            print('Found')
        else:
            print('Not Found')


    def search_recur(self, root, search_item):
        if root != None:
            if search_item < root.data:
                return self.search_recur(root.left, search_item)
            elif search_item > root.data:
                return self.search_recur(root.right, search_item)
            else:
                return 1


    def deletion(self, root, delete_item):
        if root !=  None:
            if delete_item < root.data:
                root.left = self.deletion(root.left, delete_item)
            elif delete_item > root.data:
                root.right = self.deletion(root.right, delete_item)
            else:
                return None
        
        return root


t = Tree()
t.insert(50)
t.insert(20)
t.insert(15)
t.insert(70)
t.insert(35)
t.insert(10)

print('Inorder Traversal : ', end = ' ')
t.inorder(t.root)
print()

print('Preorder Traversal : ', end = ' ')
t.preorder(t.root)
print()

print('Postorder Traversal : ', end = ' ')
t.postorder(t.root)
print()

# t.search_iter(t.root, 35)

if t.search_recur(t.root, 70) == 1:
    print('Found')
else:
    print('Not Found')

new_t = t.deletion(t.root, 15)
t.inorder(new_t)
print()