from requests import delete


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


	def get_height(self, root):
		if root == None:
			return 0
		return max(self.get_height(root=root.left), self.get_height(root.right)) + 1


	def get_height_iterative(self, root):
		queue = [[self.root, 1]]
		temp = 0
		while len(queue) > 0:
			t = queue[0]
			item, depth = t[0], t[1]
			depth = max(temp, depth)
			if item.left:
				queue.append([item.left, depth + 1])
			if item.right:
				queue.append([item.right, depth + 1]), 

			queue = queue[1:]
		
		return depth

	def height_iterative(self):
		depth = self.get_height_iterative(self.root)
		print('Height using Iteration -> ', depth)


	def height(self):
		h = self.get_height(self.root)
		print('Height using recursion -> ', h)

	
	def deepest_node(self):
		queue = [self.root]

		while len(queue) > 0:
			node = queue[0]

			if node.left != None:
				queue.append(node.left)

			if node.right != None:
				queue.append(node.right)

			queue = queue[1:]

		print('Deepest Node value -> ', node.data)

	
	def no_of_leaves(self):
		queue = [self.root]
		num = 1
		while len(queue) > 0:
			node = queue[0]
			
			if node.left != None:
				queue.append(node.left)
				num += 1

			if node.right != None:
				queue.append(node.right)
				num += 1

			queue = queue[1:]
		
		print('No. of leaves -> ', num)

	# Not working
	def reverse_bst(self):
		queue = [self.root]
		stack = [[self.root]]

		while len(queue) > 0:
			node = queue[0]

			if node.left != None:
				queue.append(node.left)

			if node.right != None:
				queue.append(node.right)

			queue = queue[1:]
			# print(queue)
			stack.append(queue)

		# print(stack)
		# for i in stack:
		# 	for j in i:
		# 		print(j.data, end= ' ')


	def get_maximum(self):
		queue = [self.root]
		max_value = self.root.data

		while len(queue) > 0:
			node = queue[0]

			if node.data > max_value:
				max_value = node.data

			if node.left != None:
				queue.append(node.left)

			if node.right != None:
				queue.append(node.right)

			queue = queue[1::]

		print('Maximum value -> ', max_value)
				

	def search_data_helper(self, root, search_data):
		# print(root.data, search_data)
		if root.data == search_data:
			return 'Found!'
		if root.left != None:
			f = self.search_data_helper(root.left, search_data)
			if f:
				return f
		if root.right != None:
			f = self.search_data_helper(root.right, search_data)
			if f:
				return f


	def search_element(self, search_data):
		output = self.search_data_helper(self.root, search_data)
		if output:
			print(output)
		else:
			print('Not Found!')



	def get_inorder_predecessor_helper(self, root):
		if root.right != None:
			return self.get_inorder_predecessor_helper(root.right)
		return root


	def get_inorder_predecessor(self, item):
		if item.right:
			node = self.get_inorder_predecessor_helper(item.left)
			return node
		return item


	# Using BFS Traversal
	def search_element_iteration(self, data):
		queue = [self.root]
		while len(queue) > 0:
			item = queue[0]

			if item.data == data:
				print('Found!')
				return

			if item.left:
				queue.append(item.left)
			if item.right:
				queue.append(item.right)

			queue = queue[1:]

		print('Not Found!')


	def delete_node_helper(self, root, data):
		if root.left:
			if root.left.data == data:
				return root
			f = self.delete_node_helper(root.left, data)
			if f:
				return f


		if root.right:
			if root.right.data == data:
				return root
			f = self.delete_node_helper(root.right, data)
			if f:
				return f


	def delete_node(self, data):
		f = self.delete_node_helper(self.root, data)
		if f:
			print(f.data)

			if f.left.data == data:
				pred = self.get_inorder_predecessor(f.left)
				print(pred.data)

				# print(f.left.data)

				f.left.data = pred.data
				del pred

				print("Node Deleted!")
				

			if f.right.data == data:
				pred = self.get_inorder_predecessor(f.right)
				# print(pred.data)

				# print(f.left.data)

				f.right.data = pred.data
				del pred

				print("Node Deleted!")
				
		else:
			print('Not Found!')


		


bst = BST()

bst.add(5)
bst.add(4)
bst.add(7)
bst.add(2)
bst.add(3)
bst.add(6)
bst.add(14)
bst.add(15)
bst.add(16)
bst.add(10)
bst.add(11)
bst.add(12)
bst.add(13)

# bst.add(1)
# bst.add(2)
# bst.add(3)
# bst.add(4)
# bst.add(5)
# bst.add(6)
# bst.add(7)


print('PreOrder -> ', end='')
bst.preorder()

print('InOrder -> ',  end='')
bst.inorder()

print('PostOrder -> ',  end='')
bst.postorder()

print('LevelOrder -> ',  end='')
bst.levelorder()

bst.height()
bst.height_iterative()
bst.deepest_node()
bst.no_of_leaves()
# bst.reverse_bst()
bst.get_maximum()

search_num = 5
print(f'Searching for {search_num} ->', end = ' ')
bst.search_element(search_num)

# bst.get_inorder_predecessor()

search_num = 147
print(f'Searching for {search_num} using iteration ->', end = ' ')
bst.search_element_iteration(search_num)

bst.delete_node(14)

print('InOrder -> ',  end='')
bst.inorder()