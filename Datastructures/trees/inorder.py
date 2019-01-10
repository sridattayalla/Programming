#making a tree

class tree :
	def __init__(self, key) :
		self.key = key
		self.right = None
		self.left = None

def attach(depth, n):
	if depth <= 10 :
		tree.key = n * 2
		tree.right = attach(depth + 1, )
		tree.left = None
	