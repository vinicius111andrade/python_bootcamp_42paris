'''
https://www.w3schools.com/python/python_dictionaries.asp
https://docs.python.org/3/library/stdtypes.html#dict

value = dic["key"]
dic["key"] = new_value
dic_copy = dic.copy()
dic_keys = list(dic)

Recipe for cake:
Ingredients list: ['flour', 'sugar', 'eggs']
To be eaten for dessert.
Takes 60 minutes of cooking.
'''

cookbook_00 = { 'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10},
			 'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
			 'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}}


def		dic_keys(dic):
	return (list(dic))

def		print_recipe(dish, cookbook):
	dic_dish = cookbook[dish]

	print("Recipe for {}:".format(dish))
	print("Ingredients list: {}".format(dic_dish['ingredients']))
	print("To be eaten for {}.".format(dic_dish['meal']))
	print("Takes {} minutes of cooking.".format(dic_dish['prep_time']))

def		main():
	print_recipe('cake', cookbook_00)


main()