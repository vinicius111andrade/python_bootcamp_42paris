'''
phrase = "The right format"
Write a program to display the string above right-aligned with '-' padding and a total length of 42 characters:

> python kata03.py | cat -e
--------------------------The right format%
> python kata03.py | wc -c
    42
'''

phrase = "The right format"

size = len(phrase)

if size < 42:
    print((42 - size) * "-", phrase, sep='', end='')