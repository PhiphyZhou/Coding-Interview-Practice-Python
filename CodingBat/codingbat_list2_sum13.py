# Problem: http://codingbat.com/prob/p167025 
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the 
# number 13 is very unlucky, so it does not count and numbers that come immediately after a  
# 13 also do not count.


# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6


def sum13(ls):
    result = 0
    i = 0
    while(i<len(ls)):
        if ls[i] == 13:
            while(i<len(ls) and ls[i] == 13):
                i += 1
            i += 1
            continue
        result += ls[i]
        i += 1
    return result


print sum13([])
print sum13([1,2,3])
print sum13([1, 2, 2, 1, 13]) 
print sum13([13])
print sum13([1,13,4,5,1])
print sum13([1,13,13,13,2,1])