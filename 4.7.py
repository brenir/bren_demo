#4.7.py
#	translate 100-point grade,90-100:A,80-89:B,70-79:C,60-69:D,<60:F

def main():
	score = input("Enter an integer score, between 0 and 100: ")
	grade = chr(5-(score/60)*(2+(score-60)/10-score/100)+ord("A"))
	print "The grade is",grade
	
main()