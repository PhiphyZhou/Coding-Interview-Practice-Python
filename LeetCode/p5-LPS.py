# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution(object):
    

    def growSubstring(self, k, j,s):
                    
        while(k>=0 and j<len(s) and s[k]==s[j]):
            k = k-1
            j = j+1
            
        if(self.l<j-k-1):
            self.l = j-k-1
            self.imin = k+1
            self.imax = j-1
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.l = self.imin = self.imax = 0
    
        for i in xrange(len(s)):
            if(i>0 and i<len(s)-1 and s[i-1]==s[i+1]):
                self.growSubstring(i-1,i+1,s)

            if(i<len(s)-1 and s[i]==s[i+1]):
                self.growSubstring(i,i+1,s)
            
        return s[self.imin:self.imax+1]
        

        