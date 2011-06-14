from Euler import *

count = 0

for i in range(6,101):
	for j in range(2,i):
		if C(i,j)>10**6:
			count +=1
	
print count
