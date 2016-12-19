# 433. Minimum Genetic Mutation (Twitter)
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
# 
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
# 
# Note:
# 
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.

# Solution: breadth first search

from collections import deque

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        
        if start == end: return 0
        
        self.letters = ["A", "C", "G", "T"]
        
        # rebuild the bank using set
        bank = set(bank)
        
        if end not in bank:
            return -1
        
        queue = deque()
        queue.append((start,0))
        if start in bank:
            bank.remove(start)

        while queue:
            start, depth = queue.popleft()
            for i in range(len(start)):
                for c in self.letters:
                    if c != start[i]:
                        change = start[:i]+c+start[i+1:]
                        if change == end:
                            return depth + 1
                        if change in bank:
                            queue.append((change, depth+1))
                            bank.remove(change)
        return -1
            
  
        
        
        
        
        