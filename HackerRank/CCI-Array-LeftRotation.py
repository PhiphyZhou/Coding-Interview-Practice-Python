# Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
# Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.


def array_left_rotation(a, n, k):
    result = []
    for i in range(n):
        idx = (i+k) % n
        result.append(a[idx])
    return result
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

