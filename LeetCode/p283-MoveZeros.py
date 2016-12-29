# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# 
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):

	# better solution: inserting 
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in nums:
            if i != 0:
                nums[p] = i
                p += 1
        for j in range(p,len(nums)):
            nums[j] = 0
 
 	# The following method uses two pointers and swap and is slower.            
    def moveZeroes_2pointers(self, nums):
        p = q = 0
        p, q = self.move(p, q, nums)
        while p < len(nums) and q < len(nums):
            # print p, q, nums
            self.swap(p, q, nums)
            p, q = self.move(p, q, nums)
            
    def move(self, p, q, nums):
        while p < len(nums):
            if nums[p] == 0: break
            p += 1
        while q < len(nums):
            if nums[q] != 0 and q > p:
                break
            q += 1
        return p, q
        
    def swap(self, p, q, nums):
        temp = nums[p]
        nums[p] = nums[q]
        nums[q] = temp
            