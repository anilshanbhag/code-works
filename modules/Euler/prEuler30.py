n=4
sumAll = 0
for i in range(10,300000):
	s = sum([int(m)**5 for m in str(i)])
	if s==i:
		sumAll += i

print sumAll
