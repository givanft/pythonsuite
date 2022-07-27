"""
========================================================================================
	This is NUTRITION FACTS problem

	Implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, 
	per the FDA's poster for fruits. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
	Ignore any input that isn't a fruit.


fruits = {"Apple":130, "Avocado":50, "Banana":110, "Cantaloupe":50, "Grapefruit":60, "Grapes":90, "Honeydew Melon":50, "Kiwifruit":90, "Lemon":15, 
			"Lime":20, "Nectarine":60, "Orange":80, "Peach":60, "Pear":100, "Pineapple":50, "Plums":70, "Strawberries":50,
			"Sweet Cherries":100, "Tangerine":50, "Watermelon":80
			}

user_fruit = input("What's fruit? ").rstrip().lower().title()

#print(user_fruit)

try:
	print(fruits[user_fruit])
except:
	print(end="")
"""





"""
========================================================================================
	This is VANITY PLATES problem
	
	In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. 
	Among the requirements, though, are:

		"All vanity plates must start with at least two letters."
		"... vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
		"Numbers cannot be used in the middle of a plate; they must come at the end. 
			For example, AAA222 would be an acceptable ... vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'."
		"No periods, spaces, or punctuation marks are allowed."

	Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
	Assume that any letters in the user's input will be uppercase.
	Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
	Assume that s will be a str.

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(title):

	# --------------------------------------------
	if len(title) < 2 or len(title) > 6: 
		return False

	# --------------------------------------------
	if title.isupper() == False: 
		return False

	# --------------------------------------------
	if title[0:2].isdigit() == True: 
		return False;

	# --------------------------------------------
	if title.isalnum() == False: 
		return False

	# --------------------------------------------
	if title[(len(title)-1)].isalpha() == True:
		
		for c in title:
			if c.isdigit():
				return False
	
	# --------------------------------------------
	met_digit = False
	for c in title:
		
		if c.isdigit() == True:
			met_digit = True
			if int(c) == 0:
				return False

		if met_digit == True:
			break

	# --------------------------------------------
	no_alpha_allowed = False
	for c in title:
		
		if c.isdigit() == True:
			no_alpha_allowed = True
		else:
			if no_alpha_allowed == True:
				return False

	return True

main()
"""



"""
========================================================================================
	This is JUST SETTING UP MY TWTTR problem
	
	Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
	whether inputted in uppercase or lowercase.

twitt_message = input().strip()
modified_twitt = ""

for c in twitt_message:
	if c in ['a','e','i','o','u','A','E','I','O','U']: continue
	else:
		modified_twitt += c

print(modified_twitt)
"""

"""
========================================================================================
	This is COKE MACHINE problem

	Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
	Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
	Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.

	Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

def main():
	get_pay(50)

def get_pay(price):
	while True:
		price -= insert_coin(price)
		if price > 0: continue
		else:
			print(f"Change Owed: {price * (-1)}")
			break
	
def insert_coin(n):
	while True:
		print(f"Amount Due: {n}")
		coins = int(input("Insert Coin: ").strip())
		if coins in [5, 10, 25]: return coins

main()
"""


"""
========================================================================================
	This is CAMEL CASE problem

	Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
	Assume that the user's input will indeed be in camel case.


user_var = input().strip()
modified_user_var = ""

count = -1
for c in user_var:
	count += 1
	if c.isupper():
		if count == 0:
			modified_user_var += c.lower()
		else:
			modified_user_var += '_' + c.lower()
		continue

	modified_user_var += c

print(modified_user_var)
"""