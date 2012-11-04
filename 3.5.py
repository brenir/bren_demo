#3.5.py
#	calculate the volume and surface area of a sphere

import math

def main():

	radius = input("Enter the radius of the sphere: ")
	volume = 4.0/3.0*math.pi*(radius**3)
	surface = 4.0*math.pi*(radius**2)
	print	"The volume of the sphere is ",volume
	print "The surface of the sphere is ",surface

main()
