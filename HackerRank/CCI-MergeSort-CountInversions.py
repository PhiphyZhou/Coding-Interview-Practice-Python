# Merge Sort: Counting Inversions
# https://www.hackerrank.com/challenges/ctci-merge-sort
# Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new line.


def count_inversions(a):
    temp = [None]*len(a)      
    return merge(a,0,len(a)-1,temp)

def merge(a, left, right, temp):  
    '''@return count - the number of inversions during the merge sort'''
    
    if left >= right:
        return 0
    
    count = 0
    mid = (left+right)/2
    count += merge(a,left,mid,temp)
    count += merge(a,mid+1,right,temp)
    
    l = left
    r = mid+1
    i = left
    while l <= mid and r<=right:
        if a[l]<=a[r]:
            temp[i] = a[l]
            l += 1
        else:
            temp[i] = a[r]
            r += 1
            count += mid - l + 1
        i += 1
    
    # copy the leftovers to temp and copy back to a
    temp[i:i+mid-l+1] = a[l:mid+1]
    temp[i:i+right-r+1] = a[r:right+1]
    a[left:right+1] = temp[left:right+1]   
    return count

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)

