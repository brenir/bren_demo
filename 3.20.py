#3.20.py
#	calculate the nth number in the Fibonacci sequence.

def main():
	n = input("Enter which term you want to get: ")
	out = 1L
	temp1 = 1L
	temp2 = 1L
	
	for i in range (2,n):
		out = temp1+temp2
		temp1 = temp2
		temp2 = out
		
	print "The",n,"term of Fibonacci sequence is",out
	
main()
		