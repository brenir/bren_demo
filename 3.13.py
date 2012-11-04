#3.13.py
#	calculate the area of a triagle given the length of its three sides

import math

def main():
	a,b,c = input("Enter the length of three sides of the triagle:")
	s=(float(a)+b+c)/2
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
	
	print "The area of the triagle is",area
	
main()