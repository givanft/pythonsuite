

"""
=============================
DICT
=============================
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
"""

"""
=============================
LIST
=============================
students = ["Hermione", "Harry", "Ron"]
for item in students:
    print(item)

students.sort()

print(students.pop())
print(len(students))
"""

"""
=============================
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0: 
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
"""

"""
=============================
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(n):
    print(f"{i+1} meow")
"""

"""
=============================
print("meow\n" * 3, end="")
"""

"""
=============================
for _ in range(3):
    print("meow")
"""

"""
=============================
for i in [0,1,2]:
    print("meow")
"""

"""
=============================
i = 0
while i < 3:
    print("meow")
    i += 1
"""