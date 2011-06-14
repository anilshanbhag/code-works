from __future__ import division
m = [[a*10+b,b*10+c] for a in range(1,10) for b in range(1,10) for c in range(1,10) if (a*10+b)/(b*10+c) == a/c and a/c<1]
print m
