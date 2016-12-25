# Queues: A Tale of Two Stacks
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
# implement a queue using two stacks
# Solution: You only need to refill the dequeue stack when it's empty. The run time is O(1)

class MyQueue(object):
    def __init__(self):
        self.first = [] # the enqueue stack
        self.second = [] # the dequeue stack
    
    def peek(self):
        if not self.second:
            self.refill()
        return self.second[-1]
        
    def pop(self):
        if not self.second:
            self.refill()
        return self.second.pop()
        
    def put(self, value):
        self.first.append(value)
        
    def refill(self):
        while self.first:
            self.second.append(self.first.pop())

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        

