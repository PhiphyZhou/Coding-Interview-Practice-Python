# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sub = []
        result = 0
        
        for a in s:
            if(a not in sub):
                sub.append(a)
            else:
                idx = sub.index(a)
                l = len(sub)
                if(l>result):
                    result = l
                sub[0:idx+1]=[]
                sub.append(a)


        if(result<len(sub)):
            result = len(sub)
            

        return result
                
        