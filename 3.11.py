#3.11.py
#	calculate the distance of  two points

import math

def main():
	x1,y1=input("Enter the coordinate of the first point: ")
	x2,y2=input("Enter the coordinate of the second point: ")
	
	distance=math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
	
	print "The distance of the two points is",distance
	
main()