# 2. Add Two Numbers
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = ListNode(0)
        crusor = result
        
        while (l1 != None or l2 != None):
            
            x = 0
            if(crusor.next == None):
                crusor.next = ListNode(0)
            crusor = crusor.next
            
            if(l1 != None and l2 != None):
                x = l1.val + l2.val + crusor.val
                l1 = l1.next
                l2 = l2.next
                
            elif(l1 != None):
                x = crusor.val + l1.val
                l1 = l1.next
            else:
                x = crusor.val + l2.val
                l2 = l2.next
                
            if (x<10):
                crusor.val = x
            else:
                crusor.val = x-10
                crusor.next = ListNode(1)
                
        return result.next
        