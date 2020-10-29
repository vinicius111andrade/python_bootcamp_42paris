import sys

def is_int(arg):
  try:
    int(arg)
    return True
  except:
    return False

def main():
	if len(sys.argv) != 2:
		print("ERROR")
	else:
		arg = sys.argv[1]
		if not is_int(arg):
			print("ERROR")
		else:
			number = int(arg)
			if number == 0:
				print("I'm Zero.")
			elif number % 2 == 0:
				print("I'm Even.")
			else:
				print("I'm Odd.")

main()