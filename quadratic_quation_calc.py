#hello, this is little quadratic equations calc
from numpy import sqrt
import numpy as np

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

#turning b_value to negative
b_negative = b_value * (-1)
b_negative_str = str(b_negative)
#print user input in form of quadratic equation + formatting
equation0 = "\n" + " " + str(b_value) + " +/- sqrt(" + str(b_value) + "^(2) - 4 x " + str(a_value) + " x " + str(c_value) + ")"
equation0_length = len(equation0)
equation1 = " " + equation0_length * "_"
equation2a = int(equation0_length /2) - 3
equation2b = equation2a * " " + "2 x " + str(a_value)
print(equation0)
print(equation1)
print(equation2b)

#calculation of things in bracket + denominator calculation + print equation
b_value_power = float(b_value) * 2
axcx4 = 4 * float(a_value) * float(c_value)
brackets_solution = float(b_value_power) - float(axcx4)

#turning brackets_solutions to real number
if brackets_solution < 0:
	brackets_solution = brackets_solution * -1

sqrt_value = np.sqrt(brackets_solution)
denominator = a_value * 2

#printing and formatting next equation
equation3 = "\n" + " " + str(b_value) + " +/- " + str(brackets_solution)
equation3_length = len(equation3)
equation4 = " " + equation3_length * "_"
equation5a = int(equation3_length/2) - 2
equation5b = equation5a * " " + str(denominator)
print(equation3)
print(equation4)
print(equation5b)



#calculation +/- + print

#both results

