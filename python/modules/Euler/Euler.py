from math import *

def is_prime(n):
	n=abs(n)
	if n in [0,1] or n%2==0:
		return False
	elif n==2 or n==3:
		return True
	else:
		for i in range(3,int(sqrt(n))+1,2):
			if n%i==0:
				return False
		return True

def is_perm(a,b): return sorted(str(a)) == sorted(str(b))
 
def is_palindromic(n): return str(n)==str(n)[::-1]	

def prime_sieve(n):
    candidates = list(range(n+1))
    fin = int(n**0.5)
 
    for i in xrange(2, fin+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
 
    return [i for i in candidates[2:] if i]
    
def C(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))

def P(n,r):
	return factorial(n)/factorial(n-r)

def gcd(a, b):
	if a < 0:  a = -a
	if b < 0:  b = -b
	if a == 0: return b
	if b == 0: return a
	while b != 0: 
		(a, b) = (b, a%b)
	return a

			
