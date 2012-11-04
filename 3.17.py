#3.17.py
#	sum a series of numbers entered by the user.

def main():
	n = input("Enter the amount of numbers: ")
	sum = 0
	for i in range(n):
		num = input("Enter the number: ")
		sum = sum + num
	
	print "The sum of the numbers you input is",sum
	
main()