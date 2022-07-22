name = input("What's your name? ")

match name:
	case "Harry" | "Hermione":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")

"""
=============================================
def main():
	x = int(input("What's x: "))

	if is_even(x):
		print("Even")
	else:
		print("Odd")

def is_even(n):
	return (n % 2 == 0)
	#return True if n % 2 == 0 else False
	
main
"""

"""
=============================================
score = int(input("Score: "))

if 90 <= score <= 100:
	print("Grade: A")
elif 80 <= score < 90:
	print("Grade: B")
elif 70 <= score < 80:
	print("Grade: C")
elif 60 <= score < 70:
	print("Grade: D")
else: 
	print("Grade: F")
"""

"""
=============================================
if score >= 90 and score <= 100:
	print("Grade: A")
elif score >= 80 and score <90:
	print("Grade: B")
elif score >= 70 and score <80:
	print("Grade: C")
elif score >= 60 and score <70:
	print("Grade: D")
else: 
	print("Grade: F")
"""

"""
=============================================
x = int(input("What's X? "))
y = int(input("what's Y? "))

if x != y:
	print(f"x: {x} is not equal to y: {y}")
else:
	print(f"x: {x} is equal to y: {y}")
"""

"""
=============================================
if x < y or x > y:
	print(f"x: {x} is not equal to y: {y}")
else:
	print(f"x: {x} is equal to y: {y}")
"""


"""
=============================================
if x < y:
	print(f"x: {x} is less than y: {y}")

elif x > y:
	print(f"x: {x} is greater than y: {y}")

else:
	print(f"x: {x} is equal to y: {y}")

"""