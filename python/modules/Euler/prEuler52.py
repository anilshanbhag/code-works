from itertools import permutations
ran = []

n=1
def main():
	global n
	while True:
		print "a" ,n
		ran = range(10**n,int('1' + '6'*n)+1)
		for i in ran:
			perm = permutations(str(i))
			m2m = tuple(str(i*2))
			m3m = tuple(str(i*3))
			m4m = tuple(str(i*4))
			m5m = tuple(str(i*5))
			m6m = tuple(str(i*6))
			if m2m in perm and m3m in perm and m4m in perm and m5m in perm and m6m in perm:
				print i
				return
		n+=1

main()
