# 9.1 A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 
# steps at a time. Implement a method to count how many possible ways the child can run up 
# the stairs.


def count(n):
    mem = [None]*n
    return count_hop_ways(n, mem)


def count_hop_ways(n, mem):
    if n == 0: 
        return 1
    counter = 0
    for i in range(1,4):
        if n >= i:
            if mem[n-i] == None: 
                mem[n-i] = count_hop_ways(n-i,mem)
            counter += mem[n-i]                        
    return counter


print count(0) # 1
print count(1) # 1
print count(2) # 2
print count(3) # 4
print count(4) # 7
print count(100) # 180396380815100901214157639

# The count for step n is just the sum of the previous 3 counts.