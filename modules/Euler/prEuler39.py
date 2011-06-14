maxcount=0
maxp = 11
for p in range(12,1001):
	count = 0
	for a in range(0,p/2):
		for b in range(0,p/2):
			if b**2 + a**2 == (p-a-b)**2:
				count+=1
	if count>maxcount : 
		maxp = p
		maxcount = count

print maxp
print maxcount 
