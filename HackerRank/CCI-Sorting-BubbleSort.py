# Sorting: Bubble Sort
# https://www.hackerrank.com/challenges/ctci-bubble-sort
# Given an -element array, , of distinct elements, sort array  in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:
# 
# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
numSwaps = 0

for i in range(n):
    nSwaps = 0
    for j in range(n-1):
        if a[j]>a[j+1]:
            swap(a, j, j+1)
            nSwaps += 1
    if nSwaps == 0:
        break
    numSwaps += nSwaps
    
print 'Array is sorted in {} swaps.'.format(numSwaps)
print 'First Element: {}'.format(a[0])
print 'Last Element: {}'.format(a[-1])