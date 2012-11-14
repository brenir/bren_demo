#7.4.py
#	calculate a quize score,5-A, 4-B, 3-C, 2-D, 1-F, 0-F

def pr(grade):
	print "The corresponding grade is",grade
	
def main():
	score = input("Enter the grade: ")
	if score == 5:
		 pr("A")
	elif score == 4:
		pr("B")
	elif score == 3:
		pr("C")
	elif score == 2:
		pr("D")
	elif score == 1:
		pr("E")
	elif score == 0:
		pr("F")
	else:
		print("Wrong input.")	
		
main()
	