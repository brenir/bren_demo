# 2.9.py
# 2.9.py
# 	A program to compute the value of an investment
# 	carried 10 years into the future
# 	taking inflation into account

def main():
	print "This program calculates the future value of a 10-year investment,taking inflation into account."
	
	principal = input("Enter the initial principal: ")
	inflation = input("Enter the yearly rate of inflation: ")
	apr = input("Enter the annualized initerest rate: ")
	
	for i in range(10):
		principal = principal * (1+apr)
		principal = principal/(1+inflation)
		
	print "The actual purchasing power is:",principal
	
main()