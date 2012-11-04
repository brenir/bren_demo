#3.6.py
#	calculate the cost per square inch of a circular pizza

import math

def main():
	diameter = input("Enter the diameter of the sphere: ")
	price = input("Enter the price of the pizza: ")
	surface = math.pi*((diameter/2.0)**2)
	cps = price/surface
	print	"The cost per square inch of the pizza is ",cps

main()
