# Linked Lists: Detect a Cycle
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# Solution: use the 2 pointers trick in the book CCI

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    
    if not head: return False
    
    cur1 = head
    cur2 = head.next
    
    while cur2 and cur2.next:
        if cur1 == cur2:
            return True
        cur2 = cur2.next.next
        cur1 = cur1.next
        
    return False
    