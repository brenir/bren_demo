#7.3.py
#	calculate the total wages

def main():
	rate = input("Enter the hourly rate: ")
	time = input("Enter the number of working hours in a week: ")
	wage = 0
	if time > 40:
		wage = float(rate)*1.5*(time-40)
		time = 40
	wage = float(wage) +time*rate
	
	print "Total wage of this week is:",wage
	
main()