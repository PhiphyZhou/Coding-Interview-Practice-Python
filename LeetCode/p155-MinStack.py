# 155. Min Stack ( Google Uber Zenefits Amazon Snapchat Bloomberg )
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mini = [] # min of the stack before it
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.mini or x < self.mini[-1]:
            self.mini.append(x)
        else:
            self.mini.append(self.mini[-1])
        

    def pop(self):
        """
        :rtype: void
        """
        val = self.data.pop()
        self.mini.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()