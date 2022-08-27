def main():
	greeting = input("Prompts the user for a greeting ").strip()
	print(f"${value(greeting)}")

def value(grt):
	grt = grt.strip().lower()
	if grt.startswith("h"):
		if grt.startswith("hello"):
			return 0
		else:
			return 20
	else:
		return 100

if __name__ == "__main__":
	main()
