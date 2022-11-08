MAX = 5
names = []

for _ in range(MAX):
    names.append(input("What's name? "))

print(names)

name_to_change = input("What name need to be changed? ")
new_name = input("What's new name? ")

try:
    i = names.index(name_to_change)
except ValueError:
    print(f"ERROR: {name_to_change} is not found")
else:
    names[i] = new_name

print(names)

#MAX_X = 10
#MAX_Y = 10
#
#arr = []
#arr2D = []
#
## fill LIST
#for i in range(1, MAX_X):
#    for j in range(1, MAX_Y):
#        arr.append(j)
#    arr2D.append(arr)
#    arr = []
#
## print LIST as 2D array
#for i in range(0, MAX_X-1):
#    for j in range(0, MAX_Y-1):
#        print(arr2D[i][j], end=' ')
#    print(end='\n')

