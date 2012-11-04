#3.21.py
#	compute square root using Newton's method
#	The program will prompt the user for the value to find the square root of  and the number of times to improve the guess

import math

def main():
	x = input("Enter the value to find the square root of: ")
	n = input("Enter the times to improve the guess: ")
	
	value=x/2.0
	for i in range(1,n):
		value = (value + x/value)/2
		
	print "The value given by system function is",math.sqrt(x)
	print "The value given by the program is",value
	
main()