# - GET GIF file ---------------------------
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image =Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=[images[1]], duration = 200, loop=0)


## - WRITE to CSV by DictWriter ---------------------------
#import csv
#
#name = input("What's your name? ")
#home = input("Where's your home? ")
#
#with open("studentsw.csv", "a") as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "home"])
#    writer.writerow({"home":home, "name":name})


## - READ CSV by DictReader ---------------------------
#import csv
#
#students = []
#
#with open("students.csv") as file:
#    reader = csv.DictReader(file)
#    for row in reader:
#        students.append({"name": row["name"], "home": row["home"]})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")



## - READ CSV by reader ---------------------------
#import csv
#
#students = []
#
#with open("students.csv") as file:
#    reader = csv.reader(file)
#    for name, home in reader:
#        students.append({"name": name, "home": home})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")


## - READ CSV 1 ---------------------------
#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        students.append(student)
#
#def get_name(student):
#    return student["name"]
#
##for student in sorted(students, key=get_name):
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['house']}")


#with open("students.csv") as file:
#    for line in file:
#        name, home = line.rstrip().split(",")
#        print(f"{name} is in {home}")

#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")

# - READ FILE ---------------------------
#with open("names.txt", "r") as file:
#    lines = file.readlines()
#
#for line in lines:
#    print("hello,", line.rstrip())


# - WRITE FILE ---------------------------
#name = input("What's name? ")
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

# - just LIST ---------------------------
#names = []
#
#for _ in range(3):
#    names.append(input("What's namr? "))
#
#for name in sorted(names):
#    print(f"Hello, {name}")