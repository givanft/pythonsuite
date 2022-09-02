"""
========================================================================================
	This is CS50 P-SHIRT problem
    
"""
import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1].lower()
input_ext = input_file.rpartition(".")[-1]
if input_ext not in ["jpg","png","jpeg"]:
    sys.exit("Invalid input")

output_file = sys.argv[2].lower()
output_ext = output_file.rpartition(".")[-1]
if output_ext not in ["jpg","png","jpeg"]:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    with Image.open("shirt.png") as shirt:
        size_shirt = shirt.size

        with Image.open(input_file) as input_image:
            input_image = ImageOps.fit(input_image, size_shirt)
            input_image.paste(shirt, shirt)
            input_image.save(output_file)

except FileNotFoundError:
    sys.exit(f"Input does not exist")


"""
========================================================================================
	This is SCOURGIFY problem
    
    Implement a program that:
        Expects the user to provide two command-line arguments:
            - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
            - the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
    If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

csv_read = sys.argv[1]
if csv_read[len(csv_read)-4:] != ".csv":
    sys.exit("Not a CSV file")

csv_read = sys.argv[1]
try:
    hogwarts  = []

    with open(csv_read) as file:
        reader = csv.DictReader(file)

        for row in reader:
            last, first = row["name"].split(",")
            hogwarts.append({"first":first.strip(), "last":last.strip(), "house":row["house"].strip()})

    with open(sys.argv[2], "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(hogwarts)

except FileNotFoundError:
    sys.exit(f"Could not read {csv_read}")
"""

"""
========================================================================================
	This is PIZZA PY problem

    Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio's format, 
    and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library's grid format. 
    If the user 
        - does not specify exactly one command-line argument, 
        - or if the specified file's name does not end in .csv, 
        - or if the specified file does not exist, 
        the program should instead exit via sys.exit.


import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

csv_file = sys.argv[1]
if csv_file[len(csv_file)-4:] != ".csv":
    sys.exit("Not a CSV file")

csv_file = sys.argv[1]

try:
    table = []
    header = []   

    with open(csv_file) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        reader = csv.reader(file)

        for row in reader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, header, tablefmt="grid"))
"""


"""
========================================================================================
	This is LINES OF CODE problem

	Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, 
    excluding comments and blank lines. 
    If the user:
        - does not specify exactly one command-line argument, 
        - or if the specified file's name does not end in .py, 
        - or if the specified file does not exist, 
        the program should instead exit via sys.exit.

    Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) 
    Assume that any line that only contains whitespace is blank.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_path = sys.argv[1]
if file_path[len(file_path)-3:] != ".py":
    sys.exit("Not a Python file")

try:
    code_lines = 0

    with open(file_path) as file:
        for line in file:
            
            line = line.strip()
            if len(line) == 0:
                continue
            
            if line.startswith("#") == True:
                continue   
            
            code_lines += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(code_lines)
"""