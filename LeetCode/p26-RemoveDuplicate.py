# 26. Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        diff = 0
        prev = None
        
        for x in nums:
            if(prev==None or prev!=x):
                diff += 1
                nums[diff-1] = x
                prev = x
                
        return diff