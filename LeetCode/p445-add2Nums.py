# 445. Add Two Numbers II (Bloomberg, Microsoft)
# You are given two linked lists representing two non-negative numbers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # store the references of each node into array
        arr1 = []
        arr2 = []
        cursor = l1
        while(cursor):
            arr1.append(cursor.val)
            cursor = cursor.next
        cursor = l2
        while(cursor):
            arr2.append(cursor.val)
            cursor = cursor.next
        
        result = None
        carry = 0
        while arr1 or arr2:
            sum = carry
            if arr1: sum += arr1.pop()
            if arr2: sum += arr2.pop()
            carry, val = divmod(sum,10)
            # print carry, val
            digit = ListNode(val)
            digit.next = result
            result = digit

        if carry>0:
            digit = ListNode(1)
            digit.next = result
            result = digit
        
        return result