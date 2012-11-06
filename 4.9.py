#4.9.py
#	calculatethe numerologist of a name

import string
def main():
	name = raw_input("Enter a name: ")
	name = string.lower(name)
	num = 0
	for ch in name:
		num = num + ord(ch)-ord("a")+1
	print "The numerologist of the name is ",num
	
main()