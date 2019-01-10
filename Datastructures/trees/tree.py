class Node :
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		
	#method to insert 
	def insert(self, data):
		if self.key:
			if self.key > data:
				if  self.left == None:
					self.left = Node(data)
				else :
					self.left.insert(data)
			elif self.key < data:
				if self.right == None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.key = Node(data) 
		
	#method to print tree
	def PrintTree(self):
		if self.left != None:
			self.left.PrintTree()
		print(self.key)
		if self.right != None:
			self.right.PrintTree()
			
		


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()



