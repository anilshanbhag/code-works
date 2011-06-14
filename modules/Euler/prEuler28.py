sumAll = 1
sequence = [((2*i+1)**2)*4 - 12*i for i in range(1,501)]
for j in sequence: sumAll +=  j

print "Pr28 ans : %d" % sumAll
