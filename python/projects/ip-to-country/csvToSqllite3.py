import sqlite3

def main():
	con = sqlite3.connect('ip-to-country.db')
	c = con.cursor()
	c.execute('''create table iptable
	(start, end, ccode, cshort, country)''')
	f = open('ip-to-country.csv')
	for line in f.readlines():
		parts = line.strip('\r\n').strip('"').split('","')
		query = """insert into iptable values (%d, %d, "%s", "%s", "%s")""" % (int(parts[0]),int(parts[1]),parts[2],parts[3],parts[4])
		c.execute(query)
	con.commit()
	c.close()
	
if __name__ == '__main__':
	main()

