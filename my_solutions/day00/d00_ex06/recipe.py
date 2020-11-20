'''
https://www.w3schools.com/python/python_dictionaries.asp
https://docs.python.org/3/library/stdtypes.html#dict

value = dic["key"]
dic["key"] = new_value
dic_copy = dic.copy()
dic_keys = list(dic)

Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
'''

def		dic_keys(dic):
	return (list(dic))

def		print_recipe(recipe, cookbook):
	dic_recipe = cookbook[recipe]

	print()
	print("Recipe for {}:".format(recipe))
	print("Ingredients list: {}".format(dic_recipe['ingredients']))
	print("To be eaten for {}.".format(dic_recipe['meal']))
	print("Takes {} minutes of cooking.".format(dic_recipe['prep_time']))
	print()

def		print_cookbook(cookbook):
	recipes_list = dic_keys(cookbook)
	for recipe in recipes_list:
		print_recipe(recipe, cookbook)

def		print_recipes_list(cookbook):
	recipes_list = dic_keys(cookbook)
	print("Recipes: ", recipes_list)

def		isinCookbook(recipe, cookbook):
	recipes_list = dic_keys(cookbook)
	for i in range(len(recipes_list)):
		if recipe == recipes_list[i]:
			return(True)
	return (False)

def		ask_ingredients():
	run = True
	ingredients_list = []
	while run:
		print("Add another ingredient?")
		another = input("Yes or No?\n")
		if another == "Yes":
			ingredient = input("Ingredient name: ")
			ingredients_list.append(ingredient)
		elif another == "No":
			run = False
		else:
			print("Answer Yes or No please.")
	if ingredients_list == []:
		print("Ingredients list is empty, try again...")
		ingredients_list = ask_ingredients()
	return (ingredients_list)

def		isMealtype(meal):
	meal_types = ["breakfast", "lunch", "dinner", "dessert", "snack"]
	for i in range(len(meal_types)):
		if meal == meal_types[i]:
			return(True)
	return (False)

def		ask_meal_type():
	run = True
	while run:
		print("What kind of meal is it? Meal types I know are breakfast, lunch, dinner, dessert, snack. Choose one please.")
		meal_type = input("Meal type is: ")
		if not isMealtype(meal_type):
			print("I don't know this kind of meal, please select one of the meal types displayed.")
		else:
			run = False
	return (meal_type)

def is_int(arg):
  try:
    int(arg)
    return True
  except:
    return False

def		isPreptime(prep_time):
	it_is_int = is_int(prep_time)
	correct = False
	if it_is_int:
		prep_time = int(prep_time)
		if prep_time > 0:
			correct = True
	return (correct)

def		ask_prep_time():
	run = True
	while run:
		print("How many minutes does it take to prep this meal? Only positive integers please.")
		prep_time = input("Prep time is: ")
		if not isPreptime(prep_time):
			print("Please type a positive integer to represent prep time in minutes please.")
		else:
			run = False
	return (prep_time)

def		add_recipe(recipe, cookbook):
	ingredients_list = ask_ingredients()
	meal_type = ask_meal_type()
	prep_time = int(ask_prep_time())
	recipe_details = {}
	recipe_details["ingredients"] = ingredients_list
	recipe_details["meal"] = meal_type
	recipe_details["prep_time"] = prep_time
	cookbook[recipe] = recipe_details

def		del_recipe(recipe, cookbook):
	del cookbook[recipe]

def		print_prompt():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def		main():
	cookbook_00 = { 'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10},
			 'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
			 'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}}
	run = True
	while run:
		print_prompt()
		cmd = input()
		if cmd == "1": #what to do when recipe typed is on dict?
			print("The cookbook already has...")
			print_recipes_list(cookbook_00)
			recipe = input("Name of the recipe to add: ")
			if isinCookbook(recipe, cookbook_00):
				print("Recipe already in cookbook...")
			else:
				add_recipe(recipe, cookbook_00)
		elif cmd == "2":
			print()
			print_recipes_list(cookbook_00)
			recipe = input("Select recipe to delete: ")
			if isinCookbook(recipe, cookbook_00):
				del_recipe(recipe, cookbook_00)
			else:
				print("Recipe not in cookbook...")
			print()
		elif cmd == "3":
			print()
			print_recipes_list(cookbook_00)
			recipe = input("Select recipe to print: ")
			if isinCookbook(recipe, cookbook_00):
				print_recipe(recipe, cookbook_00)
			else:
				print("Recipe not in cookbook...")
			print()
		elif cmd == "4":
			print_cookbook(cookbook_00)
		elif cmd == "5":
			print("\nCookbook closed.")
			run = False
		else:
			print("This option does not exist, please type the corresponding number.")
			print("To exit, enter 5.")
	




main()