# Describe how you could use a single array to implement three stacks.

# Let's try to implement k stacks dynamically using one array
# The solution in version 4 of the CCI book is not correct. Instead of using one "indexUsed" variable, 
# we need to use a list to store the unused indices. 
# Here I use the python list as a stack to store the unused indices.  

# Note that in order to use one array as several stacks, we need to triple the space of 
# the array to store extra informations. This is not very useful for small size data types.
# However, when each element of the data is a large object, this can be useful.


class Stacks:
	def __init__(self, total_size, num_stacks):
		self.array = [None]*total_size # the data array
		self.tops = [-1]*num_stacks # tops of each stack
		self.next = [None]*total_size # index of the next element in the stack
		self.free = [] # a simple stack to store the free to use indices
		for i in xrange(total_size):
			self.free.append(total_size-i-1)
	
	def push(self, stack, value):
		if len(self.free)==0: 
			print "Stack Overflow!"
			sys.exit(1)
		idx = self.free.pop()
		self.array[idx] = value
		self.next[idx] = self.tops[stack]
		self.tops[stack] = idx
		
	def pop(self, stack):
		if self.isEmpty(stack):
			print "Stack " + str(stack) + " is empty!"
			return None
		top = self.tops[stack]
		value = self.array[top]
		self.array[top] = None
		self.tops[stack] = self.next[top]
		self.next[top] = None
		self.free.append(top)
		return value
	
	def peek(self, stack):
		return self.array[self.tops[stack]]
		
	def isEmpty(self, stack):
		return self.tops[stack] == -1
	
	def __str__(self):
		s = str(self.array) + '\n' + str(self.next)
		return s
		
	def get_stack(self, stack):
		ls = []
		top = self.tops[stack]
		while(top!=-1):
			ls.append(self.array[top])
			top = self.next[top]
		return ls
		
	
stacks = Stacks(10, 3)
stacks.push(0,1)
stacks.push(1,2)
stacks.push(0,3)
stacks.pop(1)
stacks.pop(1)
stacks.push(1,5)
stacks.push(2,14)
stacks.push(0,6)
stacks.push(2,20)
stacks.pop(1)
print stacks
print stacks.get_stack(0)
print stacks.get_stack(1)
print stacks.get_stack(2)




		