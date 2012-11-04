#3.16.py
#	calculate the sum of the squares for the first n natural numbers.

import math

def main():
	print "The program will calculate the sum of the squares of the first n natural numbers."
	n = input("Enter the number n : ")
	
	sum = 0
	for i in range(1,n+1):
		sum = sum + math.sqrt(i)
		
	print "The sum of the squares is",sum
	
main()