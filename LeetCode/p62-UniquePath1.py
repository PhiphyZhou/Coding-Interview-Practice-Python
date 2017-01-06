# 62. Unique Paths (Bloomberg)
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?

# Note: using combinatorial, we can get a formula for the answer: (m+n-2)!/((n-1)!(m-1)!)
# We can instead compute the formula using iteration

# Solution using O(n) space
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        minlen = min(m, n)
        maxlen = max(m, n)
        
        if minlen == 1:
            return 1
        
        arr = [1]*minlen
        for i in range(maxlen-1):
            for j in range(1, minlen):
                arr[j] = arr[j-1] + arr[j]
                
        return arr[minlen-1]
            
     
        