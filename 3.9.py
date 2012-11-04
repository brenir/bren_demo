#3.9.py
#	calculate the cost of a order

def main():
	pounds = input("Enter the pounds of coffee you want to order: ")
	cost = 10.50*pounds+1.50+0.86*pounds
	print "The total cost of this order is",cost
	
main()	