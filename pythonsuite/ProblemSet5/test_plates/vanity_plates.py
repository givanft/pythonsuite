def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(title):

	# --------------------------------------------
	#if len(title) < 2 or len(title) > 6:
	#	return False

	# --------------------------------------------
	if title.isupper() == False:
		return False

	# --------------------------------------------
	if title[0:2].isalpha() == False:
		return False;

	# --------------------------------------------
	if title[0:2].isdigit() == True:
		return False;

	# --------------------------------------------
	if title.isalnum() == False:
		return True#False

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

if __name__ == '__main__':
	main()
