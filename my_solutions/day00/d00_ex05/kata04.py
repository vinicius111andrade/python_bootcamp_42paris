'''
( 0, 4, 132.42222, 10000, 12345.67)
Given the tuple above, return the following result:

> python kata04.py
day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
'''

tup = 0, 4, 132.42222, 10000, 12345.67

print("day_{:02d}, ex_{:02d} : {:.2f}, ".format(tup[0], tup[1], tup[2]), sep='', end='')
print("{:.2e}, {:.2e}".format(tup[3], tup[4]), sep='', end='')