# -----------------------------------------------------------
def main():
	p = convert(input("What's fraction (X/Y)? ").rstrip())
	print(f"{gauge(p)}")

# -----------------------------------------------------------
def convert(fraction):
	while True:
		try:
			x, y = int(fraction.split("/")[0]), int(fraction.split("/")[1])

			if y == 0:
				raise ZeroDivisionError
			
			if x > y:
				raise ValueError

			break
		except (ValueError, ZeroDivisionError):
			raise

	return round((x / y) * 100)

# -----------------------------------------------------------
def gauge(percentage):
	if percentage >= 99:
		return "F"
	elif percentage <= 1:
		return "E"

	return str(percentage) + "%"

# -----------------------------------------------------------
if __name__ == "__main__":
	main()