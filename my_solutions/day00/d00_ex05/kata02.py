'''
(3,30,2019,9,25)
Given the tuple above, whose values stand for: (hour, minutes, year, month, day), write a program that displays it in the following format:

> python kata02.py
09/25/2019 03:30
'''

tup = 3, 30, 2019, 9, 25
# hh, mm, yyyy, mm, dd

output = ""

for i, nb in enumerate(tup):
	if i < 2:
		output += "{:02d}".format(nb) + "/"
	elif i == 2:
		output += "{}".format(nb) + " "
	elif i == 3:
		output += "{:02d}".format(nb) + ":"
	else:
		output += "{:02d}".format(nb)

print(output)