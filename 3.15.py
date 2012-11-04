#3.15.py
#	calculate the sum of the first n natural numbers,where the value of n is provided by the user

def main():

	print "The program will calculate the sum of the first n natural numbers."
	n = input("Enter the number n: ")
	
	sum = 1
	for i in range(1,n+1):
		sum=sum*i
		
	print "The sum of the first",n,"natural numbers is",sum
	
main()