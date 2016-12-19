# 84. Largest Rectangle in Histogram
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# exceeds time limit
class Solution(object):
    def largestRectangleArea_n2(self, heights):
        """
        Not accepted: time O(n^2), space O(n)
        :type heights: List[int]
        :rtype: int
        """
        marea = 0
        n = len(heights)
        arr = [None]*n
        for i in range(n):
            for j in range(i,n):
                if j == i:
                    mh = heights[i]
                    area = heights[i]
                    arr[i] = (area, mh)
                    if area > marea: marea = area
                else:
                    if heights[j] >= arr[j-1][1]:
                        area = arr[j-1][0]+arr[j-1][1]
                        arr[j] = (area, arr[j-1][1])
                        if area > marea: marea = area
                    else:
                        area = (j-i+1)*heights[j]
                        arr[j] = (area, heights[j])
                        if area > marea: marea = area
        return marea