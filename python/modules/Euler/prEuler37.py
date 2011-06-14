from Euler import *
m = prime_sieve(10000000)
a = []

lst = ['0','2','4','6','8']
#Filter
for i in m:
	temp = str(i)
	if not any([j in temp for j in lst]):
		a.append(i)
#Append
result = [23]
for i in a:
	if len(str(i)) == 1:
		continue
	flag = 1
	m = list(str(i))
	while len(m)>=2:
		del m[0]
		if not int(''.join(m)) in a:
			flag=0
			break
	if not flag:
		continue	
	m = list(str(i))
	while len(m)>=2:
		del m[len(m)-1]
		if not int(''.join(m)) in a:
			flag=0
			break
	if flag:
		result.append(i)

print result
print sum(result)	 
