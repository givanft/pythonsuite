def main():
	twitt_message = input().strip()
	print(shorten(twitt_message))

def shorten(msg):
	modified_twitt = ""
	for c in msg:
		if c in ['a','e','i','o','u']:#,'A','E','I','O','U']: 
			continue
		else:
			modified_twitt += c
	return modified_twitt

if __name__ == "__main__":
	main()