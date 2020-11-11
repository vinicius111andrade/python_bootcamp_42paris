'''
t = (19,42,21)
Including the tuple above in your file, write a program that dynamically builds up a formatted string like the following:

> python kata00.py
The 3 numbers are: 19, 42, 21
'''

t = (19, 42, 21)

size = len(t)
i = 1
first_part = f"The {size} numbers are:"
second_part = ""

for i in range(size):
	if i < (size - 1):
		second_part += str(t[i]) + ", "
	else:
		second_part += str(t[i])

print(first_part, second_part)