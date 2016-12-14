# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # convert the array into a dictionary. It may throw away index of the same number
        dnums = {nums[i]:i for i in xrange(len(nums))} 
        print dnums
        
        # iterate the dict, find the difference of the element and the target, and check if it's in dnums
        for i in xrange(len(nums)):
            diff = target-nums[i]
            # print diff
            if (diff in dnums and i!=dnums[diff]): # the 2nd condition is to avoid finding the same number twice
                return [i,dnums[diff]]
        return None 
        
def main():
	solution = Solution()
	print solution.twoSum([0,4,3,0],0)
    
if __name__ == "__main__":
	main() 