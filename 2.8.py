# 2.8.py
# 	A program to convert Fahrenheit temps to Celsius

def main():
		fah = input("What is the Fahrenheit temperature? ")
		cel = (fah-32.0)*5.0/9.0
		print "The temperature is", cel, "degrees Celsius."
		
main()