'''
A bounch of tree classes
'''

class BinarySearchTree:
	''' The Node of a binary search tree
	'''
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
	def insert_node(self,value):
		''' Insert a node to the tree rooted at this node
		'''
		if(value <= self.value): 
			if not self.left:
				self.left = BinaryNode(value)
			else:
				self.left.insert_node(value)
		else: 
			if not self.right:
				self.right = BinaryNode(value)
			else:
				self.right.insert_node(value)
		
	def get_height(self):
		''' Return the height of the subtree rooted at this node.
			The height of a single node is 0.
		'''
		height = 0
		if(self.left): height = self.left.get_height() + 1
		if(self.right): 
			height = max(height, self.right.get_height() + 1)
		return height
	
	def preorder_traversal(self, ls):
		''' get the value of each node of the subtree in
			preorder: parent->left->right
		'''
		ls.append(self.value)
		if(self.left): self.left.preorder_traversal(ls)
		if(self.right): self.right.preorder_traversal(ls)
		
	def preorder_print(self):
		''' print the values of the subtree in preorder
		'''
		ls = []
		self.preorder_traversal(ls)
		print ls
	
	def inorder_traversal(self, ls):
		''' get the value of each node of the subtree in
			ineorder: left->parent->right
		'''
		if(self.left): self.left.inorder_traversal(ls)
		ls.append(self.value)
		if(self.right): self.right.inorder_traversal(ls)
		
	def inorder_print(self):
		''' print the values of the subtree in preorder
		'''
		ls = []
		self.inorder_traversal(ls)
		print ls
		
bst = BinarySearchTree(5)
for i in [7,4,6,2,8,1,3,9,5]:
	bst.insert_node(i)
bst.inorder_print()
print bst.get_height()
	
	
	
	
	
	
	
	
	
	
	
	
	
	