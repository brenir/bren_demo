#3.14.py
#	determine the length of a ladder required to reach a given height when leaned against a house

import math

def main():
	height = input("Enter the height of the ladder: ")
	angle = input("Enter the angle of the ladder: ")
	len = float(height)/math.sin(math.pi*angle/180)
	
	print "The required length of the ladder is",len

main()