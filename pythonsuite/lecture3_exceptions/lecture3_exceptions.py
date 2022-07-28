"""
======================================

"""
def get_bool():
	try:
		return True
	finally:
		return False

	return True

print(f"{get_bool()}")

"""
======================================

def main():
	print(f"x is {get_num()}")

def connection_db():
	raise ConnectionError


def get_num():
	x = -1
	while True:
		try:
			#x = 10*(1/0)
			#x = 10*(1/'k')
			#x = 10*(1/z)
			#raise NameError("Very bad deal")
			connection_db()
		except (ZeroDivisionError, TypeError, NameError, ConnectionError) as err:
			print(f"Error type: {type(err)}")
			print(f"Error args: {err.args}")
			print(f"Error text: {err}")
			break

	return x

main()
"""

"""
======================================

def main():
	print(f"x is {get_num()}")

def get_num():
	while True:
		try:
			return int(input("What's X? "))
		except :
			pass

main()
"""

"""
======================================

def main():
	print(f"x is {get_num()}")

def get_num():
	while True:
		try:
			return int(input("What's X? "))
		except :
			print("X is not a number !")

main()
"""

"""
======================================

while True:
	try:
		x = int(input("What's x? "))
	except ValueError:
		print("x is not an integer")
	else:
		break

print(f"x is {x}")
"""



"""
======================================

try:
	x = int(input("What's x? "))
except ValueError:
	print("x is not an integer")
else:
	print(f"x is {x}")
"""