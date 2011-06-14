from Euler import *
from math import *
lst = range(3,10000,2)

primes = []

for i in lst:
	#print "a" , i
	if is_prime(i):
		primes.append(i)
	else:
		c=1
		m = int(sqrt(i/2)) + 1
		while(c<=m):
			if is_prime(i - 2*c**2):
				break
			else:
				c+=1
			 
			if c==m and not is_prime(i - 2*c**2):
				print i
