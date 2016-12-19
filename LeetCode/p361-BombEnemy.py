# 361. Bomb Enemy (Google)
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.


# The following solution exceeds the time limit
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        rnum = len(grid)
        if rnum < 1: return 0
        cnum = len(grid[0])
        if cnum < 1: return 0
        rlist = [-1, -1, 0] # 1D: W or -1,  W or len, value
        clist = [ [-1, -1, 0] for j in range(cnum)]  # 2D
        maxval = 0
        
        for i in range(rnum):
            rlist = [-1, -1, 0]
            for j in range(cnum):
                
                if grid[i][j] == 'E':
                    continue
                if grid[i][j] == 'W':
                    rlist[0] = j
                    clist[j][0] = i
                    continue

                if j < rlist[1]:
                    rowval = rlist[2]
                else:
                    rowval = 0
                    for k in range(rlist[0]+1, cnum):
                        if grid[i][k] == 'E':
                            rowval += 1
                        elif grid[i][k] == 'W':
                            rlist[1] = k               
                            break
                        if k == cnum - 1:
                            rlist[1] = cnum
                    rlist[2] = rowval         
                   
                if i < clist[j][1]:
                    colval = clist[j][2]
                else:
                    colval = 0 
                    for k in range(clist[j][0]+1, rnum):
                        if grid[k][j] == 'E':
                            colval += 1
                        elif grid[k][j] == 'W':
                            clist[j][1] = k
                            break
                        if k == cnum - 1:
                            clist[j][1] = rnum
                    clist[j][2] = colval        

                val = rowval + colval
                if maxval < val:
                    maxval = val

        return maxval 
                 
