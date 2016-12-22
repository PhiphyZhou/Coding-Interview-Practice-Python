# Trees: Is This a Binary Search Tree?
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
# Given the root node of a binary tree, can you determine if it's also a binary search tree?

# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# solution 1
# inorder traversal and put each element in an array, then check if the array is in order
def inord(arr, root):
    if root.left:
        inord(arr, root.left)
#    print root.data
    arr.append(root.data)
    if root.right:
        inord(arr, root.right)

        
def check_binary_search_tree_1(root):
    arr = []
    inord(arr, root)
#    print arr
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]: return False
    return True

# solution 2
# don't use extra array, compare during the inorder traversal 
flag = True
prev = None

def check_inorder(root):
	global flag, prev
	if not flag: return 
	if root.left:
		check_inorder(root.left)
	if prev:
		if root.data <= prev:
			flag = False
			return
	prev = root.data
	if root.right:
		check_inorder(root.right)
		
def check_binary_search_tree_2(root):
	check_inorder(root)
	f = flag
	return f
  
def buildTree():
	
	root = node(3)
	root.left = node(2)
	root.right = node(6)
	
	l = root.left
	r = root.right
	
	l.left = node(1)
	l.right = node(4)
	
	r.left = node(5)
	r.right = node(7)
	
	return root


r = buildTree()
print check_binary_search_tree_2(r)
