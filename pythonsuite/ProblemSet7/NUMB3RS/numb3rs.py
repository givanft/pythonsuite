import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    matches = re.search(r"^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$", ip, re.IGNORECASE)

    if matches is None:
        return False

    for index in range(4):
        if int(matches.group(index+1)) > 255:
            return False
    
    return True

if __name__ == "__main__":
    main()
