# Implement an algorithm to find the nth to last element of a singly linked list.
# implement using recursion.

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def find_nth(head, pos):
	if head == None:
		return 0, None # 0 is the index from the tail
	idx, node = find_nth(head.next, pos)
	idx += 1
	if idx == pos:
		node = head
	return idx, node

def build_list(lst):
	if len(lst)<1:
		return None
	head = ListNode(lst[0])
	cursor = head
	for v in lst[1:]:
		cursor.next = ListNode(v)
		cursor = cursor.next
	return head
		
head = build_list([1,2])
idx, node = find_nth(head, 1)
print node.val

	