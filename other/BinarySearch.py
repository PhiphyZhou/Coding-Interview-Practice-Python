# recursive implementation of binary search


def binary_search(A, val, offset):
    if len(A) == 0: return None
    m = len(A)/2
    if val == A[m]: return m+offset
    elif val < A[m]: 
        idx = binary_search(A[:m],val,0)
        if idx == None: return None
        else:
            return offset + idx
    else:
        idx = binary_search(A[m+1:],val,m+1)
        if idx == None: return None
        else:
            return offset + idx
        
A = [1,2,3,4,5,6]
print binary_search(A,10,0)