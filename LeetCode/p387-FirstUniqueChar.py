# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = [0]*26
        for l in s:
            idx = ord(l) - ord('a')
            counter[idx] += 1
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if counter[idx] == 1:
                return i
        return -1