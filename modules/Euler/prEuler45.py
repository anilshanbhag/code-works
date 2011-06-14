from math import sqrt
 
def is_pentagonal(n):
  p = (sqrt(1 + 24*n) + 1) / 6
  return p==int(p)
 
h = lambda n: n*(2*n - 1) #calculate the nth hexagonal number
 
n = 144 
while not(is_pentagonal(h(n))): n += 1 
 
print "Answer to PE45 = ",h(n)
