import sys

def join_args_into_str(args_list):
	string = ""
	for arg in args_list:
		string = string + arg
	return(string)

def reverse_str_order(string):
	reversed_string = ""
	i = len(string) - 1
	while i >= 0:
		reversed_string = reversed_string + string[i]
		i = i - 1
	return(reversed_string)

def reverse_str_capitalization(string):
	return (string.swapcase())

def main():
	if len(sys.argv) < 2:
		print()
	else:
		string = join_args_into_str(sys.argv[1:])
		if len(string) == 0:
			print()
		else:
			reversed_string = reverse_str_order(string)
			result = reverse_str_capitalization(reversed_string)
			print(result)
main()