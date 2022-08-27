"""
========================================================================================
	This is OUTDATED problem

	Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
	wherein the month in the latter might be any of the values in the list below (see month_list).
	Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in either format, prompt the user again. 
	Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""
month_list = [
				"January",
				"February",
				"March",
				"April",
				"May",
				"June",
				"July",
				"August",
				"September",
				"October",
				"November",
				"December"
				]

# --------------------------------------------------------------
def check_format(dt):
	if len(user_date.split('/')) == 3 and len(user_date.split()) == 1:
		return 1

	if len(user_date.split(',')) == 2 and len(user_date.split()) == 3:
		return 2

	return 0
	
# --------------------------------------------------------------	
while True:
	user_date = input("What's date? ").rstrip().lower()
	#user_date = "September 8, 1636"

	match check_format(user_date):
		case 0:
			continue
		case 1:
			try:
				m, d, y = user_date.split('/')
				m = int(m)
				d = int(d)
				y = int(y)
			except ValueError:
				continue

			if (m < 1 or m > 12) or (d < 1 or d > 31) or (y < 1 or y > 9999):
				continue

			break
		case 2:
			user_date = user_date.replace(', ', ' ')

			try:
				m, d, y = user_date.split()
				m = m.capitalize()
				d = int(d)
				y = int(y)
			except ValueError:
				continue

			if m not in month_list:
				continue

			m = int(month_list.index(m) + 1)

			if (d < 1 or d > 31) or (y < 1 or y > 9999):
				continue

			break

print(f"{y}-{m:02}-{d:02}")



"""
========================================================================================
	This is GROCERY LIST problem

	Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one's input to a program). 
	Then output the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. 

grocery_list = {}

while True:
	try:	
		grocery_item = input("What's item? ").rstrip().lower()
		
		if grocery_item in grocery_list:
			grocery_list[grocery_item] += 1
		else:
			grocery_list[grocery_item] = 1
	except EOFError:
		break

for item in sorted(grocery_list):
	print(grocery_list[item], item.upper())
 """


"""
========================================================================================
	This is FELIPE'S TAQUERIA problem

	One of the most popular places to eat in Harvard Square is Felipe's Taqueria, which offers a menu of entrees, per the dict below, 
	wherein the value of each key is a price in dollars.
	Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one's input to a program). 
	After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
	Treat the user's input case insensitively. Ignore any input that isn't an item. Assume that every item on the menu will be titlecased.

entrees = {	"Baja Taco": 4.00, 
			"Burrito": 7.50, 
			"Bowl": 8.50, 
			"Nachos": 11.00, 
			"Quesadilla": 8.50,
			"Super Burrito": 8.50, 
			"Super Quesadilla": 9.50, 
			"Taco": 3.00, 
			"Tortilla Salad": 8.00
			}

sum_total = 0.0

while True:
	
	try:
		user_item = input("What's entree? ").rstrip().lower().title()
	
		sum_total += entrees[user_item]
	except KeyError:
		pass
	except EOFError:
		break
	else:
		print("${:.2f}".format(sum_total))
"""




"""
========================================================================================
	This is FUEL GAUGE problem

	Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
	For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

	Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
	and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
	If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
	And if 99% or more remains, output F instead to indicate that the tank is essentially full.

	If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
	Be sure to catch any exceptions like ValueError or ZeroDivisionError.


while True:
	try:
		tank_fill = input("What's fraction (X/Y)? ").rstrip()

		x, y = int(tank_fill.split("/")[0]), int(tank_fill.split("/")[1])

		if y ==0:
			raise ZeroDivisionError
		
		if x > y:
			raise ValueError
		
		break
	except (ValueError, ZeroDivisionError):
		pass

percent_fill = round((x / y) * 100)

if percent_fill >= 99:
	print("F")
elif percent_fill <= 1:
	print("E")
else:
	print (f"{percent_fill}%")
"""