# futval.py
# 	A program to compute the value of an investment
# 	The years of the investment will be input by the user

def main():
	print "This program calculates the future value of a investment in the future."
	years = input("Enter the years of the investment: ")
	principal = input("Enter the initial principal: ")
	apr = input("Enter the annualized interest rate: ")
	
	for i in range(years):
		principal = principal * (1 + apr)
		
	print "The amount in",years,"years is:",principal
		
main()