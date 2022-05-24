"""
Functions:
    1. insert
    2. insert_helper
    3. inorder
    4. preorder
    5. postorder
    6. levelorder
    7. search_iter : search using iteration
    8. search_recure : search using recursion
    9. deletion
    10. height
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

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

        self.size += 1

    
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


    def levelorder(self, root):
        print(root.data, end= ' ')
        queue = [root]

        while len(queue) > 0:
            temp = queue[0]

            if temp.left != None:
                queue.append(temp.left)
                print(temp.left.data, end= ' ')

            if temp.right != None:
                queue.append(temp.right)
                print(temp.right.data, end= ' ')

            queue = queue[1:]

        
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

    def inorder_successor(self, root):
        
        if root.right == None:
            print('No inorder successor')
            return

        root = root.right
        while root.left:
            root = root.left
        
        print('Inorder successor -> ', root.data)
        return root


    def deletion(self, root, delete_item):
        if root !=  None:
            if delete_item < root.data:
                root.left = self.deletion(root.left, delete_item)
            elif delete_item > root.data:
                root.right = self.deletion(root.right, delete_item)
            else:
                # case 1: No child
                if root.left == None and root.right == None:
                    self.size -= 1
                    return None

                # case 2: Atleast one child
                if root.left != None and root.right == None:
                    self.size -= 1
                    return root.left

                if root.left == None and root.right != None:
                    self.size -= 1
                    return root.right

                # case 3: Two children
                else:
                    self.size -= 1
                    in_succ = self.inorder_successor(root)
                    root.data = in_succ.data
                    root.right = self.deletion(in_succ, in_succ.data)

        return root


    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


    def get_element_level(self, element):
        queue = [(self.root, 0)]

        while len(queue) > 0:

            for i in queue:
                print(i[0].data, i[1])

            temp = queue[0]

            if temp[0].data == element:
                return temp[1]

            if temp[0].left != None:
                l = temp[1] + 1
                queue.append((temp[0].left, l))

            if temp[0].right != None:
                l = temp[1] + 1

                queue.append((temp[0].right, l))
            
            queue = queue[1:]

        return 'Not Found!'

            

t = Tree()
t.insert(50)
t.insert(20)
t.insert(15)
t.insert(70)
t.insert(35)
t.insert(10)
t.insert(100)
t.insert(65)
t.insert(45)
t.insert(5)
t.insert(46)
t.insert(47)

print('Inorder Traversal : ', end = ' ')
t.inorder(t.root)
print()

print('Preorder Traversal : ', end = ' ')
t.preorder(t.root)
print()

print('Postorder Traversal : ', end = ' ')
t.postorder(t.root)
print()

print('Levelorder Traversal : ', end = ' ')
t.levelorder(t.root)
print()


num = 70
if t.search_recur(t.root, num) == 1:
    print(f'Found {num}')
else:
    print(f'Not Found {num}')


num = 35
size = t.size
t.root = t.deletion(t.root, num)
if size == t.size:
    print(f'Not Deleted! {num}')
else:
    print(f'Deleted! {num}')

print('Inorder :', end = ' ')
t.inorder(t.root)
print()

# print('Height : ', t.height(t.root))
# print('Level : ', t.get_element_level(100))