cont = []

for i in range(2,101):
	for j in range(2,101):
		if not i**j in cont:
			cont.append(i**j)

print "Ans for pr 29: %d" % len(cont)
