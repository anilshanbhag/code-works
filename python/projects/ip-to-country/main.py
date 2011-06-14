import sqlite3
import sys

if __name__ == '__main__':
	if sys.argv[1]:	ip = sys.argv[1]
	else:
		print "Enter Ip Address eg: 117.114.12.1"
		ip = raw_input()
	ipParts = ip.split('.')
	if len(ipParts) != 4: print "Invalid Ip"
	else:	
		ipNum = sum([int(ipParts[i])*256**(3-i) for i in range(0,4)])
		print ipNum
		con = sqlite3.connect('ip-to-country.db')
		c = con.cursor()
		c.execute("select country from iptable where start<=? and end>=?", (ipNum, ipNum))
		result = c.fetchone()
		if result: print "This IP is from %s " % result[0]
		else: print "This IP is reserved or unused or invalid" 	
		c.close()		 	



