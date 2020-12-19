'''
Using list comprehensions, you will have to make a program that removes all the words in a 
string that are shorter than or equal to n letters, and returns the filtered list with no punctuation.

The program will accept only two parameters: a string, and an integer n.

> python filterwords.py "Hello, my friend" 3
['Hello', 'friend']
'''

import sys

def is_int(arg):
	try:
		int(arg)
		return True
	except:
		return False

def is_letter(arg):
	if arg.isalpha():
		return True
	else:
		return False

def filterwords(string, min_len):
	i = 0
	new_word = ""
	list_of_words = []
	while i < len(string):
		while (not is_letter(string[i])):
			i += 1
		while (i < len(string) and is_letter(string[i])):
			new_word += string[i]
			if (i < len(string)):
				i += 1
		if len(new_word) >= min_len:
			list_of_words.append(new_word)
			new_word = ""
		else:
			new_word = ""
	return (list_of_words)

def main():
	if len(sys.argv) != 3:
		print("ERROR")
	elif is_int(sys.argv[1]) or not is_int(sys.argv[2]):
		print("ERROR")
	else:
		list_of_words = filterwords(sys.argv[1], int(sys.argv[2]))
		print(list_of_words)

main()
