#Time : 16s
from Euler import *
from itertools import permutations
lst = [i for i in prime_sieve(10000) if i>1000]

diffmap = []

for i in range(0,len(lst)-1):
	for j in range(i+1,len(lst)):
		if lst[j]*2-lst[i] in lst:
			diffmap.append([lst[i],lst[j],lst[j]*2-lst[i]])

for m in diffmap:
	if tuple(str(m[1])) in permutations(str(m[0])) and tuple(str(m[2])) in permutations(str(m[0])):
		print m
