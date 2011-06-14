def cut(n):
	m = n
	for i in range(0,n-1):
		m *= n
		m = m%10**10
	return m

sumAll = sum([cut(i) for i in range(1,1001)])
print sumAll%10**10		
