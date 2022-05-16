class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None
	

	def insert(self, root, new_node):
		if new_node.data < root.data:
			if not root.left:
				root.left = new_node
			else:
				self.insert(root.left, new_node)

		elif new_node.data > root.data:
			if not root.right:
				root.right = new_node
			else:
				self.insert(root.right, new_node)


	def add(self, data):
		new_node = Node(data)

		if self.root == None:
			self.root = new_node
		
		else:
			self.insert(self.root, new_node)


	def get_preorder(self, root):
		if root:
			print(root.data, end = ' ')
			self.get_preorder(root.left)
			self.get_preorder(root.right)


	def get_inorder(self, root):
		if root:
			self.get_inorder(root.left)
			print(root.data, end = ' ')
			self.get_inorder(root.right)


	def get_postorder(self, root):
		if root:
			self.get_postorder(root.left)
			self.get_postorder(root.right)
			print(root.data, end = ' ')
		

	def preorder(self):
		self.get_preorder(self.root)
		print()


	def inorder(self):
		self.get_inorder(self.root)
		print()


	def postorder(self):
		self.get_postorder(self.root)
		print()

	
	def levelorder(self):
		queue = [self.root]

		while len(queue) > 0:
			item = queue[0]
			if item.left:
				queue.append(item.left)
			if item.right:
				queue.append(item.right)

			print(item.data, end=' ')
			queue = queue[1:]
		print()


bst = BST()

bst.add(5)
bst.add(4)
bst.add(7)
bst.add(2)
bst.add(3)
bst.add(6)
bst.add(10)

bst.preorder()
bst.inorder()
bst.postorder()
bst.levelorder()