# 63. Unique Paths II (Bloomberg)
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.


# The solution below is O(n^2) in space. It can be optimized to O(n) as in p62
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        arr = [ [0 for i in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    arr[i][j] = 1
                elif i == 0:
                    arr[i][j] = arr[i][j-1]
                elif j == 0:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
                    
        return arr[m-1][n-1]