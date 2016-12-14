# Given a sorted array of n integers that has been rotated an unknown number of times, 
# give an O(log n) algorithm that finds an element in the array. You may assume that the 
# array was originally sorted in increasing order.

# This implementation is not finished. The following is just to find the initial element
# of the ordered list.

def find_init(ls):
	if(len(ls)==1):	
		return 0
	if(len(ls)==0):
		return None
	if(ls[0]<ls[-1]):
		print ls[0], ls[-1], "not rotated"
		return 0
	if(len(ls)==2):
		return 1
	i = len(ls)/2
	if (ls[i]>ls[0]):
		return len(ls)/2 + find_init(ls[i:])
	else:
		return find_init(ls[:i+1])
		
ls1 = [4,6,8,8,1,1,3,4]
ls2 = [1,2,3,4,5]
ls3 = [4]
print find_init(ls1)
print list("sbds")
print "s b d s".split(" ")

