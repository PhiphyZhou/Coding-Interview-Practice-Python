# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ''
        
        i = 0
        pre = ''
        
        while(1):
            if (len(strs[0])<i+1):
                return pre
            ref = strs[0][i]
            for j in xrange(1,len(strs)):
                if(len(strs[j])<i+1 or strs[j][i]!=ref):
                    return pre
                    
            pre += ref
            i += 1