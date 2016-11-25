# Implement an algorithm to determine if a string has all unique characters. What if you 
# can not use additional data structures?

def isUniqueChar2(s):
	counts = [0]*256
	for c in s:
		ci = ord(c)
		print ci
		print chr(ci)
		print str(ci)
		if counts[ci] > 0:
			return False 
		counts[ci] += 1
	return True
	
if __name__ == '__main__':
	s = 'abcsdfs'
	print isUniqueChar2(s)