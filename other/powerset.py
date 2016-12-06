# Implement a powerset of a given set S as an array
# Solution: 
# recursively add one element to the set, union with the previous powerset.

import copy

def add_one_element(ps, e):
    ''' ps is a powerser, 2D array
       e is the element to be added to each subarray of ps    
    '''
    result = copy.deepcopy(ps)
    for s in result:    
        s.append(e)
    return result
	

def powerset(s): # implemented as a generator
    if len(s) == 0: 
    	yield []
    	return
    ps = powerset(s[1:])
#     return add_one_element(ps,s[0]) + ps
	# modify to use yield instead to save memory
    for i in ps:
		yield i
		yield i + [s[0]]

def powerset_it(s): # iterative implementation
	include = [False]*len(s)
	result = []
	while(True):
		print result
		for i in range(len(s)-1,-2,-1):
			if i == -1: return 
			if include[i] == False:
				include[i] = True
				result.append(s[i])
				break
			include[i] = False
			result.pop()
		
			
s0 = []
# print list(powerset(s0))
s1 = ['a']    
# print list(powerset(s1))
s2 = ['a','b']
# print list(powerset(s2))
s3 = ['a','b','c']
# print list(powerset(s3))

powerset_it(s3)
