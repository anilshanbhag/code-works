pent = [i*(3*i-1)/2 for i in range(2,3000)]

for i in range(3,3000):
	for j in range(2,i):
		if 	(pent[i] + pent[j]) in pent and (pent[i] - pent[j]) in pent:
			print pent[i] - pent[j]
