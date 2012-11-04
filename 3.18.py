#3.18.py
#	find the average of a series of numbers entered by the user.

def main():
	n = input("Enter the amount of numbers: ")
	sum = 0
	for i in range(n):
		num = input("Enter the number: ")
		sum = sum + num
	
	ave = float(sum)/n
	print "The average of the numbers you input is",ave
	
main()