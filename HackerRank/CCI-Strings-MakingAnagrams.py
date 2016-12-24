# Strings: Making Anagrams
# https://www.hackerrank.com/challenges/ctci-making-anagrams
# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

def number_needed(a, b):
    s1 = buildDict(a)
    s2 = buildDict(b)
    
    total = 0
    for c,v in s1.items():
        if s2.has_key(c):
            total += abs(v-s2[c])
            del s1[c], s2[c]
        else:
            total += v
            del s1[c]
    for v in s2.values():
        total += v
    
    return total

def buildDict(a):
    s = {}
    for c in a:
        s[c] = s.get(c,0)+1
    return s

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)