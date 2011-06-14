import re
from Euler import *

a = prime_sieve(100000)
refined = []

pat = re.compile('(0.*0|1.*1|2.*2|3.*3|4.*4|5.*5|6.*6|7.*7|8.*8|9.*9)')

for i in a:
	if pat.match(str(i)):
		refined.append(i)

print refined
