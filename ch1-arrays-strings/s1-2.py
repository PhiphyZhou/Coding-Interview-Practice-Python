# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as  
# characters, including the null character.)

def reverse(s):
	ending = ''
	if(s[-1]=='\0'):
		print 'haha'
		ending = '\0'
		l = list(s[:-1]) 
	else:
		l = list(s)
		
	l.reverse()
	return ''.join(l)+ending

def reverse2(s):
	i = 0
	j = len(s)
	if(s[-1]=='\0'):
		j -= 1
	while(i<j):
		temp = s[i]
		s[i] = s[j]
		s[j] = temp
		i += 1
		j -= 1
		
	
if __name__ == '__main__':
	s = 'abcsdfs\0'
	print reverse2(s)
