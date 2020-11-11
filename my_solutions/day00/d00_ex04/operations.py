'''
> python operations.py 10 3
Sum:         13
Difference:  7
Product:     30
Quotient:    3.3333333333333335
Remainder:   1
'''
import sys

def		example():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("    python operations.py 10 3")

if len(sys.argv) > 3:
	print("InputError: too many arguments\n")
	example()
	exit(0)
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print("Sum:         ", a + b)
	print("Difference:  ", a - b)
	print("Product:     ", a * b)
	print("Quotient:    ", a / b)
	print("Remainder:   ", a % b)
except IndexError:
	example()
except ValueError:
	print("InputError: only numbers\n")
	example()
except ZeroDivisionError:
	print("Quotient:     ERROR (div by zero)")
	print("Remainder:    ERROR (div by zero)")