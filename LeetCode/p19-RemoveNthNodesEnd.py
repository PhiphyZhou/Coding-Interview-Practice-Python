# 19. Remove Nth Node From End of List
# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        nodes = []
        cursor = head
        while(cursor!=None):
            nodes.append(cursor)
            cursor = cursor.next
        
        idx = len(nodes) - n
        
        if(idx==0):
            head = head.next
        elif(n==1):
            nodes[-2].next = None
        else:
            nodes[idx-1].next = nodes[idx+1]
        
        return head