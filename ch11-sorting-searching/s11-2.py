# Write a method to sort an array of strings so that all the anagrams are next to each other.

# method: use sorted() to sort the strings, by redefining the key as the sorted letter string. 

	
def sort_ana(strs):
	for s in strs:
		print sorted(s)
	return sorted(strs, key=lambda x : sorted(x))
	
if __name__ == '__main__':
	strs = ['abs','sba','sdfg','','sg','','gs']
	print sort_ana(strs)