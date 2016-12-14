# 11. Container With Most Water

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_v = 0
        s = 0
        e = len(height)-1
        
        while(s<e):
            vol = (e-s)*min(height[s],height[e])
            if(vol>max_v):
                max_v = vol
            if(height[s]<height[e]):
                s += 1
            else:
                e -= 1

        return max_v