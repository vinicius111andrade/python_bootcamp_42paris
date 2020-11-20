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

def give_word_len(arg):
	i = 0
	while (arg[i].isalpha()):
		i += 1
	return (i)

def give_new_word(word_len, string):
	new_word = ""
	i = 0
	while i < word_len:
		new_word += string[i]
	return (new_word)

def filterwords(string, min_len):
	i = 0
	word_len = 0
	new_word = ""
	list_of_words = []
	while i < len(string):
		while (not string[i].isalpha()):
			i += 1
		print(i)
		word_len = give_word_len(string[i:])
		new_word = give_new_word(word_len, string[i:])
		list_of_words.append(new_word)
		i += word_len
	return (list_of_words)

def main():
	if len(sys.argv) != 3:
		print("ERROR")
	elif is_int(sys.argv[1]) or not is_int(sys.argv[2]):
		print("ERROR")
	else:
		list_of_words = filterwords(sys.argv[1], sys.argv[2])
		print(list_of_words)

main()