"""
========================================================================================
	This is MEAL TIME problem

	In meal.py, implement a program that prompts the user for a time and outputs whether it's breakfast time, lunch time, or dinner time. 
	Suppose that you're in a country where it's customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
	If it's not time for a meal, don't output anything at all. 
	Assume that the user's input will be formatted in 24-hour time as #:## or ##:##. 
	And assume that each meal's time range is inclusive. 
	For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.

"""
def main():
	mealTime = input("What time is it? ").strip() # 7:00

	flTime = convert(mealTime)

	if 7 <= flTime <= 8:
		print("breakfast time ")

	if 12 <= flTime <= 13:
		print("lunch time ")

	if 18 <= flTime <= 19:
		print("dinner time ")

def convert(tm):
	hours, minutes = tm.split(":")
	return (float(hours) + float(minutes)/60.0)

main()



"""
========================================================================================
	This is MATH INTERPRETER problem

	In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
	calculates and outputs the result as a floating-point value formatted to one decimal place. 
	Assume that the user's input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
		x is an integer
		y is +, -, *, or /
		z is an integer
	For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

primer = input("Set arithmetic expression in format: x y z => ").strip() #1 + 2

x = float(primer.split()[0])
action = primer.split()[1]
y = float(primer.split()[2])

match action:
	case "+":
		print(x+y)
	case "-":
		print(x-y)
	case "*":
		print(x*y)
	case "/":
		if y == 0:
			y = 1.0
		print(x/y)
"""


"""
========================================================================================
	This is FILE EXTENSIONS problem

	In a file called extensions.py, implement a program that prompts the user for the name of a file and then 
	outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:
		.gif
		.jpg
		.jpeg
		.png
		.pdf
		.txt
		.zip
	If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

name = input("File name: ").lower().strip()

cn = name.count(".")
if cn == 0:
    name = name + ".xxx"
    cn = cn + 1

ext = name.split(".")[cn]
match ext:
	case "gif" | "png":
		print(f"image/{ext}")
	case "jpg" | "jpeg":
		print(f"image/jpeg")
	case "pdf" | "zip":
		print(f"application/{ext}")
	case "txt":
		print("text/plain")
	case _:
		print("application/octet-stream")
"""


"""
========================================================================================
	This is HOME FEDERAL SAVINGS BANK problem

	In a file called bank.py, implement a program that prompts the user for a greeting.
	If the greeting starts with "hello", output $0.
	If the greeting starts with an "h" (but not "hello"), output $20.
	Otherwise, output $100.
	Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.

greeting = input("Prompts the user for a greeting ").strip().lower()

if greeting.startswith("h"):
	if greeting.startswith("hello"):
		print("$0")
	else:
		print("$20")
else:
	print("$100")
"""

"""
========================================================================================
	This is DEEP THOUGHT problem

	In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
	the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

myStr = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
match myStr:
	case "42" | "forty-two" | "forty two":
		print("Yes")
	case _:
		print("No")
"""