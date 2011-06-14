from Euler import *
import itertools

a = prime_sieve(1000000)
result = []

def genRotate(n):
	final = []
	st = list(str(n))
	for i in range(0,len(st)):
		st.append(st[0])
		del st[0]
		final.append(int(''.join(st)))
	return final

for i in a:
	if not i in result:
		if all([int(j)%2 for j in str(i)]):
			perm = genRotate(i)
			flag=1
			for n in perm:
				if not n in a:
					flag=0
					break
			if flag:
				for k in perm:
					result.append(k)

print sorted(set(result))	
print len(sorted(set(result)))					
