#3.10.py
#calculate the scope of a line through two points

def main():
	x1,y1=input("Enter the coordinate of the first point: ")
	x2,y2=input("Enter the coordinate of the second point: ")
	scope=(float(y2)-float(y1))/(float(x2)-float(x1))
	print "he scope of a line through two points is",scope
	
main()