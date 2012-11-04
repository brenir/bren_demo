# 2.7.py
# A program to convert Celsius temps to Fahrenheit
#	It will print a table of changing every 10 degrees from 0C to 100C.

def main():
	print "Celsius\tFahrenheit"
	for i in range(11):
		celsius = 10.0*i
		fahrenheit = 9.0/5.0 * celsius + 32
		print celsius,"\t",fahrenheit
		
main()