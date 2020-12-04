import random

def		main():
	intro_1 = "This is an interactive guessing game!\n"
	intro_2 = "You have to enter a number between 1 and 99 to find out"
	intro_3 = " the secret number.\n"
	intro_4 = "Type 'exit' to end the game.\nGood luck!"
	print(intro_1 + intro_2 + intro_3 + intro_4)

	not_exit = True
	not_found = True
	nb_trials = 0
	while (not_exit and not_found):
		str_in = input()
		print()

main()
