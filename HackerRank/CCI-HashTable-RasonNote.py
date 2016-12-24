# Hash Tables: Ransom Note
# https://www.hackerrank.com/challenges/ctci-ransom-note
# A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.
# 
# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

def ransom_note(magazine, rasom):
    md = counter(magazine)
    rd = counter(rasom)
    
    for k,v in rd.items():
        mv = md.get(k,0)
        if mv < v:
            return False
        
    return True

def counter(ls):
    d = {}
    for e in ls:
        d[e] = d.get(e,0) + 1
    return d

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"