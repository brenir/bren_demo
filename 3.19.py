#3.19.py
#	The program will approximates the value of pi, the number of terms of sum up will be input by the user.

def main():
	n = input("Enter the number of terms: ")
	sum = 0
	
	for i in range(n):
		sum = sum + ((-1)**(i%2))*4.0/(2*i+1)
		
	print "The approxiate value after",n,"times' sum up is",sum
	
main()