"""
==========================================
	This is TIP problem
"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
	return float(d.removeprefix('$'))
    # TODO

def percent_to_float(p):
	return (float(p.removesuffix('%'))/100)
    # TODO

main()

"""
==========================================
	This is EINSTEIN problem

mass = int(input("m: "));
print(f"E: {mass*pow(300000000, 2)}")
"""

"""
==========================================
	This is FACES problem

def main():
	myStr = input();
	print(convert(myStr))

def convert(myStr):
	return myStr.replace(":)", "🙂").replace(":(", "🙁")

main()
"""

"""
==========================================
	This is PLAYBACK problem

myStr = input()
print(myStr.replace(" ", "..."))
"""

"""
==========================================
	This is INDOOR problem

myStr = input()
print(myStr.lower())
"""





