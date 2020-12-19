import random

def		is_end(string):
	if string == "exit":
		return True
	else:
		return False

def is_int(arg):
	try:
		int(arg)
		return True
	except:
		return False

def		is_valid_input(string):
	valid = True

	if not is_int(string):
		valid = False
	elif not (1 <= int(string) <= 99):
		valid = False

	if not valid:
		print("\nPlease enter an integer between 1 and 99.")
	return valid

def		intro_msg():
	intro_1 = "This is an interactive guessing game!\n"
	intro_2 = "You have to enter a number between 1 and 99 to find out"
	intro_3 = " the secret number.\n"
	intro_4 = "Type 'exit' to end the game.\nGood luck!\n"
	print(intro_1 + intro_2 + intro_3 + intro_4)

def		congrats_msg(nb_trials):
	print("Congratulations, you've got it!")
	print(f"You won in {nb_trials} attempts!")

def		is_found(secret_nb, guess):
	if secret_nb == guess:
		return True
	else:
		return False

def		main():
	end = False
	found = False
	nb_trials = 0
	guess = 0
	secret_nb = int(random.randint(1, 99))

	intro_msg()
	while (not end and not found):
		str_in = input("Your guess: ")
		end = is_end(str_in)
		nb_trials += 1
		if not end and is_valid_input(str_in):
			guess = int(str_in)
			found = is_found(secret_nb, guess)
	if(found):
		congrats_msg(nb_trials)

main()
