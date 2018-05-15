#hello, this is little quadratic equations calc
import math

a_value = None
b_value = None
c_value = None

while (a_value and b_value and c_value) == None:
	try:
		#user input for a, b, c values
		a_value=float(input("Enter 'a' value: "))
		b_value=float(input("Enter 'b' value: "))
		c_value=float(input("Enter 'c' value: "))
	#exception catch if it is not a value
	except ValueError:
			print("It wasn't a numerical value, please input again")
#print user input in form of quadratic equation
equation0 = ("\n-" + str(b_value) + " +/- sqrt(" + str(b_value) + "^(2) - 4 x " + str(a_value) + " x " + str(c_value) + ")")
equation0_length = len(equation0)
equation1 = equation0_length * "_"
equation2a = int(equation0_length /2) - 3
equation2b = equation2a * " " + "2 x " + str(a_value)
print(equation0)
print(equation1)
print(equation2b)

#calculation of things in bracket + denominator calculation + print equation

#calculation +/- + print

#both results

