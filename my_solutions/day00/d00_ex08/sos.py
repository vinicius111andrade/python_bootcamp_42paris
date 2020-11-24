'''
You will have to make a function which encodes strings into Morse code.
The input will accept all alphanumeric characters.
'''

import sys

int_morse_dict = {
'a' : '.-',
'A' : '.-',
'b' : '-...',
'B' : '-...',
'c' : '-.-.',
'C' : '-.-.',
'd' : '-..',
'D' : '-..',
'e' : '.',
'E' : '.',
'f' : '..-.',
'F' : '..-.',
'g' : '--.',
'G' : '--.',
'h' : '....',
'H' : '....',
'i' : '..',
'I' : '..',
'j' : '.---',
'J' : '.---',
'k' : '-.-',
'K' : '-.-',
'l' : '.-..',
'L' : '.-..',
'm' : '--',
'M' : '--',
'n' : '-.',
'N' : '-.',
'o' : '---',
'O' : '---',
'p' : '.--.',
'P' : '.--.',
'q' : '--.-',
'Q' : '--.-',
'r' : '.-.',
'R' : '.-.',
's' : '...',
'S' : '...',
't' : '-',
'T' : '-',
'u' : '..-',
'U' : '..-',
'v' : '...-',
'V' : '...-',
'w' : '.--',
'W' : '.--',
'x' : '-..-',
'X' : '-..-',
'y' : '-.--',
'Y' : '-.--',
'z' : '--..',
'Z' : '--..',
'0' : '-----',
'1' : '.----',
'2' : '..---',
'3' : '...--',
'4' : '....-',
'5' : '.....',
'6' : '-....',
'7' : '--...',
'8' : '---..',
'9' : '----.'
}

# check if only alphanum
# find first word, 69 is a word
# iterate word chars
# translate char to morse
# build morse string
# print word
# is there another word?
# yes, print " / " and go next

def is_alphanum_or_space(string):
	for i in range(len(string)):
		if not (string[i].isalnum() or string[i] == " "):
			return False
	return True

def translate_to_morse(arg_list):
	translated_list = []
	new_word = ""
	char = ""
	morse_chars = ""
#need to add a space between morse chars
	for string in arg_list:
		str_len = len(string)
		i = 0
		while i < str_len:
			if string[i] == " ":
				i += 1
			else:
				while i < str_len and string[i].isalnum():
					char = string[i]
					morse_chars = int_morse_dict[char]
					for m_char in morse_chars:
						new_word += m_char
					i += 1
				translated_list.append(new_word)
				new_word = ""
	return translated_list

def output_translation(words_list):
	list_len = len(words_list)
	i = 0

	while i < list_len:
		if i == 0:
			print(words_list[i], sep='', end='')
		elif i == list_len - 1:
			print(words_list[i], sep='', end='')
		else:
			print(" / ", sep='', end='')
			print(words_list[i], sep='', end='')
			print(" / ", sep='', end='')
		i += 1


def main():
	if len(sys.argv) == 1:
		print("Give me a alphanumeric string to translate!")
		return 0
	for item in sys.argv[1:]:
		if not is_alphanum_or_space(item):
			print("Give me only alphanumeric strings to translate!")
			return 0
	translated_words_list = translate_to_morse(sys.argv[1:])
	output_translation(translated_words_list)



main()