# 66. Plus One (Google)
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while(i>-1):
            if digits[i] < 9:
                digits[i] += 1
                break
            digits[i] = 0
            i -= 1
        if i == -1:
            digits.insert(0,1)
        return digits