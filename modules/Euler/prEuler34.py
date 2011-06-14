from math import *
fac = [factorial(i) for i in range(0,10)]

sumAll=0

for i in range(10,1000000):
	if sum([fac[int(m)] for m in str(i)]) == i:
		sumAll += i
	
print sumAll
