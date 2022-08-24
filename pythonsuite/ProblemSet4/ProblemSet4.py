"""
========================================================================================
	This is BITCOIN PRICE INDEX problem

	Implement a program that:

		- Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. 
			If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
		- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
			among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like: except requests.RequestException
		- Outputs the current cost of n Bitcoins in USD to four decimal places, using ',' as a thousands separator.
"""
import sys
import json
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
	n_bcoins = float(sys.argv[1])
except ValueError:
	sys.exit("Command-line argument is not a number")

rq = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

price = 0.0

o = rq.json()
bpi = o["bpi"]
for currency in bpi:
	if currency == "USD":
		rate = bpi[currency]
		price = n_bcoins * rate["rate_float"]
		break

print(f"${price:,.4f}")


"""
========================================================================================
	This is LITTLE PROFESSOR problem

	Implement a program that:

		- Prompts the user for a level n. If the user does not input 1, 2, or 3, the program should prompt again.
		- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. 
			No need to support operations other than addition (+).
		- Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, 
			allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
		- The program should ultimately output the user's score, a number out of 10.

from random import randint

def main():
	lv = get_level()
	
	n = 10
	score = 0
	while n > 0:
		x = generate_integer(lv)
		y = generate_integer(lv)

		attempt = 3
		while attempt > 0:
			print(f"{x} + {y} = ", end = "")

			try:
				answer = int(input().rstrip())

				if (x + y) != answer:
					raise ValueError
				else:
					break

			except ValueError:
				print("EEE")
				attempt -= 1
				continue

		if attempt == 0:
			print(f"{x} + {y} = {x+y}", end = "\n")
		else:
			score += 1

		n -= 1

	print(f"Score: {score}")


def get_level():
	while True:
		try:
			lv = int(input("Level: ").rstrip())
			
			if lv in (1, 2, 3):
				return lv
		except ValueError:
			continue



def generate_integer(level):
	if level == 1:
		return randint(0, 9)
	elif level == 2:
		return randint(10, 99)
	else:
		return randint(100, 999)


if __name__ == "__main__":
    main()
 """


"""
========================================================================================
	This is GUESSING GAME problem

	Implement a program that:

	Prompts the user for a level, n If the user does not input a positive integer, the program should prompt again.
	Randomly generates an integer between 1 and n inclusive, using the random module.
	Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
		If the guess is smaller than that integer, the program should output 'Too small!' and prompt the user again.
		If the guess is larger than that integer, the program should output 'Too large!' and prompt the user again.
		If the guess is the same as that integer, the program should output 'Just right!' and exit.

from random import randint

while True:
	try:
		level = int(input("Level: "))
		
		if level <= 0:
			continue

		level = randint(1, level)
		break
	except ValueError:
		pass

guess = 0
while guess != level:
	try:
		guess = int(input("Guess: "))

		if guess == level:
			print("Just right!")
		elif guess > level:
			print("Too large!")
		else:
			print("Too small!")
		
	except ValueError:
		pass
"""


"""
========================================================================================
	This is ADIEU, ADIEU problem

	Implement a program that prompts the user for names, one per line, until the user inputs control-d. 
	Assume that the user will input at least one name. 
	Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:

		Adieu, adieu, to Liesl
		Adieu, adieu, to Liesl and Friedrich
		Adieu, adieu, to Liesl, Friedrich, and Louisa
		Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
		Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
		Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
		Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import inflect

p = inflect.engine()

mylist = []
while True:
	try:
		mylist.append(input("Name: ").rstrip().lower().capitalize())
	except EOFError:
		break

print("Adieu, adieu, to", p.join(mylist))
"""

"""
========================================================================================
	This is FRANK, IAN AND GLEN'S LETTERS problem

	Implement a program that:

	Expects zero or two command-line arguments:
		-- Zero if the user would like to output text in a random font.
		-- Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
		   and the second of the two should be the name of the font.
	Prompts the user for a str of text.
	Outputs that text in the desired font.

	If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, 
	the program should exit via sys.exit with an error message.

import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
figlet_font = choice(figlet.getFonts())

if len(sys.argv) != 1 and len(sys.argv) != 3:
	sys.exit("Invalid usage")

if len(sys.argv) == 3:
	if sys.argv[1].rstrip().lower() in ["-f", "--font"]:
		figlet_font = sys.argv[2]
	else:
		sys.exit("Invalid usage")

if figlet_font in figlet.getFonts():
	figlet.setFont(font=figlet_font)
	print(figlet.renderText(input("What's text? ")))
else:
	sys.exit("Invalid usage")
"""

"""
========================================================================================
	This is EMOJIZE problem

	Implement a program that prompts the user for a str in English and then outputs the "emojized" version of that str, 
	converting any codes (or aliases) therein to their corresponding emoji.

from emoji import emojize
emoji_request = input("What's emoji? ").rstrip().lower()
print(emojize(emoji_request, language='alias'))
"""