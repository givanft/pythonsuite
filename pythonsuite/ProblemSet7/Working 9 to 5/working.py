import re

# ================================================================
def main():
    print(convert(input("Hours: ")))

# ================================================================
def convert(wtime):
    
    matches = re.search(r"^(\d{1,2})(?::|\s)(\d{1,2}|AM|PM)\s(AM|PM)?\s*to\s(\d{1,2})(?::|\s)(\d{1,2}|AM|PM)\s?(AM|PM)?$", wtime, re.IGNORECASE)
    
    if matches is None:
        raise ValueError
    
    p1 = None
    p2 = None
    for i in range(6):
        
        grp_value = matches.group(i+1)
        
        if grp_value is None:
            continue
        
        match i+1:
            case 1:
                h1 = int(grp_value)

            case 2:
                m1 = grp_value
                if m1.isalpha(): # if AM or PM
                    m1 = 0
                    p1 = grp_value
                    continue

                m1 = int(m1)
                if m1 >= 60:
                    raise ValueError

            case 3:
                if p1 is None:
                    p1 = grp_value

            case 4:
                h2 = int(grp_value)

            case 5:
                m2 = grp_value
                if m2.isalpha(): # if AM or PM
                    m2 = 0
                    p2 = grp_value
                    continue

                m2 = int(m2)
                if m2 >= 60:
                    raise ValueError

            case 6:
                 if p2 is None:
                    p2 = grp_value

            case _:
                continue

    # ----------------------------------
    h1 = convert_to_24(p1, h1)
    h2 = convert_to_24(p2, h2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

# ================================================================
def convert_to_24(p, h):

    if p is None or h > 12 or h == 0:
        raise ValueError

    if p.lower() == "am" and h == 12:
        h = 0

    if p.lower() == "pm" and h < 12:
        h += 12

    return h

# ================================================================
# ================================================================
if __name__ == "__main__":
    main()