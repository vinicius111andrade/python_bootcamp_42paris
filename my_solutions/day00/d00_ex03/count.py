def isPunctuation(text):
	value = False
	if text == ".":
		value = True
	elif text == ",":
		value = True
	elif text == "!":
		value = True
	elif text == ";":
		value = True
	elif text == "?":
		value = True
	elif text == "'":
		value = True
	elif text == "-":
		value = True
	return (value)

def count_everything(text):
	chars = 0
	upper = 0
	lower = 0
	punct = 0
	spaces = 0

	for i in range(len(text)):
		chars = chars + 1
		if text[i].isupper():
			upper = upper + 1
		elif text[i].islower():
			lower = lower + 1
		elif isPunctuation(text[i]):
			punct = punct + 1
		elif text[i] == " ":
			spaces = spaces + 1

	print("The text contains {} characters:".format(chars))
	print("- {} upper letters".format(upper))
	print("- {} lower letters".format(lower))
	print("- {} punctuation marks".format(punct))
	print("- {} spaces".format(spaces))

def text_analyzer(text = False):
	input_text = ""
	if text == False:
		input_text = input("What is the text to analyse?: ")
		count_everything(input_text)
	else:
		count_everything(text)