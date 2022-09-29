import sys
import re
import inflect

from datetime import date
from datetime import timedelta

# --------------------------------------------------------------------
def main():
    birth = get_birth_date(input("Data of Birth: "))

    total_minutes = (date.today()-birth).days * 24 * 60

    p = inflect.engine()
    print(f'{p.number_to_words(total_minutes, andword="").capitalize()} minutes')

# --------------------------------------------------------------------
def get_birth_date(birth):
    matches = re.search(r"(\d{4})-(\d{2})-(\d{2})", birth, re.IGNORECASE)

    try:
        if matches is None:
            raise ValueError

        return date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
    except ValueError:
        sys.exit("Invalid data")

# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
