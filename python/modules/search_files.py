"""
Module to check for content in files
"""
from os import walk,remove
from os.path import join as joinpath

__version__='0.0.1'
__author__='Anil Shanbhag (anilashanbhag@gmail.com)'

def find(rootdir,string):
	"""Find a string through files in dir tree"""
	filelist=[]
	for path,dirs,files in walk(rootdir):
		for filename in files:
			filepath = joinpath(path,filename)
			if string in file(filepath).read():
				filelist.append(filepath)
				
	return filelist
	
if __name__=='__main__':
	from argparse import ArgumentParser
    
	PARSER = ArgumentParser( description='Search through content of files.' )
	PARSER.add_argument( 'root', metavar='R', help='Dir to search.' )
	PARSER.add_argument( 'value',metavar='V', help='String to search for.')
	ARGS = PARSER.parse_args()
	DUPS = find(ARGS.root,ARGS.value)
	print '%d files found.' % len(DUPS)
	for f in sorted(DUPS):
		print '\t'+f
