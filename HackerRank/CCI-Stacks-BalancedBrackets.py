# Stacks: Balanced Brackets
# https://www.hackerrank.com/challenges/ctci-balanced-brackets
# Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES on a new line; otherwise, print NO on a new line.

def is_matched(expression):
    pair = {'{':'}','[':']','(':')'}
    stack = []
    for e in expression:
        if e == '{' or e == '[' or e == '(':
            stack.append(e)
        else:
            if not stack: # more right brackets than left
                return False
            x = stack.pop()
            if e != pair[x]:
                return False
    if stack: # more left brackets than right
        return False
    return True
            

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

