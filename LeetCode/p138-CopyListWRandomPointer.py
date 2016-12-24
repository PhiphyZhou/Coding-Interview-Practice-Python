# 138. Copy List with Random Pointer (Amazon Microsoft Bloomberg Uber)
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        new_head = RandomListNode(head.label)
        cur1 = head.next
        cur2 = new_head
        
        addrs = {}
        addrs[head] = new_head
        
        # build the ordinary linked list
        while cur1:
            cur2.next = RandomListNode(cur1.label)
            cur2 = cur2.next
            addrs[cur1] = cur2
            cur1 = cur1.next
            
        # assign the random pointers
        cur1 = head
        cur2 = new_head
        
        while cur1:
            if cur1.random:
                cur2.random = addrs[cur1.random]
            cur1 = cur1.next
            cur2 = cur2.next
            
        return new_head
            

            
            
            
            
            