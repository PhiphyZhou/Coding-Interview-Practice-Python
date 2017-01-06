# 69. Sqrt(x)  (Bloomberg Apple Facebook)
# Implement int sqrt(int x).
# Compute and return the square root of x, rounded down to integer.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: 
            raise ValueError("input must be positive")
            return 
        if x == 0: return 0
        if x == 1: return 1
        
        low = 0
        high = x

        r = x/2
        while r**2 != x:
            if r**2 > x:                    
                high = r
                r = (r+low)/2
            else:
                low = r
                r = (r+high)/2                
            if r == low:
                break
        return r
        
        
        