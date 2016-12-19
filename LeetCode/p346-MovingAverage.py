# 346. Moving Average from Data Stream (Google)

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.


from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.win = size
        self.sum = 0
        self.l = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.win == 0: return 0

        self.q.append(val)
        
        if self.win <= self.l:
            x = q.popleft()
            self.sum += (val - x)
        else:
            self.l += 1
            self.sum += val

        return self.sum / self.l
        
        

