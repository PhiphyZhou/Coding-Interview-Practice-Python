# 364. Nested List Weight Sum II (LinkedIn)
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# 
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# 
# Different from the previous question (339) where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.
# 
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        numdep = []
        self.maxDep = 0
        self.buildNum(nestedList,numdep,1)
        res = 0
        for v,d in numdep:
            res += v*(self.maxDep-d+1)
        return res
        
    def buildNum(self, ls, nd, depth):
        for e in ls:
            if e.isInteger():
                nd.append((e.getInteger(),depth))
                if self.maxDep < depth:
                    self.maxDep = depth
            else:
                self.buildNum(e.getList(),nd,depth+1)
        
        
        
        
        
        
        
        