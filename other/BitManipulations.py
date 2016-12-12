# arithmetic and bit manipulations


def compare(a, b):
    ''' compare two integers without using comparing operations
    '''
    if ((a-b) >> 31) & 1 : return -1
    if ((b-a) >> 31) & 1 : return 1
    return 0


def swap(a, i, j):
    ''' swap two integers a[i] and a[j] without using temp variables
    '''
    if i == j: return # avoid error for swapping the same variable with itself
    a[i] = a[i] ^ a[j]
    a[j] = a[j] ^ a[i]
    a[i] = a[i] ^ a[j]
    

# print compare(23456,135366)

a = [1,0]
swap(a,0,1)
print a