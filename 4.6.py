#4.6.py
#	translate 5-point grade,5-A,4-B,3-C,2-D,1-E,0-F

def main():
	score = input("Enter the score: ")
	grade = chr(5-score+ord("A"))
	print "The grade is",grade
	
main()