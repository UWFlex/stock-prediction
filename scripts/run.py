#!/usr/bin/python

import sys, getopt

def main(argv):
	try: 
		opts, args = getopt.getopt(argv,"p",["production"])
	except getopt.GetoptError:
		print("run.py")
		sys.exit(2)
	dev = True;
	for opt, arg in opts:
		if (opt in ("-p", "--production")):
			print("Running in production mode")
			dev = False;
	if (dev):
		print("Running in development mode");
	
if __name__ == "__main__":
	main(sys.argv[1:])
