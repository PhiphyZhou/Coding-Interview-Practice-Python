#In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of di erent 
# sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending 
# order of size from top to bottom (e.g., each disk sits on top of an even larger one). 
# You have the following constraints:
# (A) Only one disk can be moved at a time.
# (B) A disk is slid o  the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the  rst rod to the last using Stacks.


def move(n, fr, to, other): # move top n elements from fr to to using buffer other
	if n == 1:
		v = fr.pop()
		to.append(v)
		print s1,s2,s3
	else:
		move(n-1,fr,other,to)
		move(1,fr,to,other)
		move(n-1,other,to,fr)
		
s1 = [5,4,3,2,1]
s2 = []
s3 = []
print s1,s2,s3
move(len(s1),s1,s2,s3)
print s1,s2,s3