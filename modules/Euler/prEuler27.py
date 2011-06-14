from Euler import prime_sieve, is_prime
 
nmax = 0;
primes = prime_sieve(1000)
for a in range(-999,999,2):
  for b in primes:
    n = 1
    while is_prime(n**2 + a*n + b): n += 1
    if n>nmax: nmax, p = n, a*b
 
print "Answer to PE27 = ",p
