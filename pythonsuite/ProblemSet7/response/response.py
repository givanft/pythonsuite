from validator_collection import validators

try:
    validators.email(input("What's your email address? "))
    print("Valid")
except:
    print("Invalid")