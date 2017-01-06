# Fibonacci numbers

import time

def fib(n):
    ''' recursive'''
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)


def fib_sum(n):
    if n == 0: return 0
    return fib(n) + fib_sum(n-1)


def fibi(n):
    ''' iterative '''
    fb1 = 0
    fb2 = 1
    for i in range(n):
        fb1, fb2 = fb2, fb1+fb2
    return fb1

mem = {0:0,1:1}
def fibm(n):
    ''' recursive using memoization'''
    if n not in mem:
        mem[n] = fibm(n-1)+fibm(n-2)
    return mem[n]

def timer(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print "time elapsed: " + str(end - start)
    print result

timer(fibm, 40)    
timer(fibi, 40)
timer(fib, 40)







