num1 = "63"
num2 = "90"

num1_max = num1[0]
num1_min = num1[1]
if num1_max < num1[1]:
    num1_max = num1[1]
    num1_min = num1[2]

num2_max = num2[0]
num2_min = num2[1]
if num2_max < num2[1]:
    num2_max = num2[1]
    num2_min = num2[2]



combo = num1 + num2

num1_max = num1[0]
num1_min = num1[1]
if num1[1] > num1_max:
    num1_max = num1[1]
    num1_min = num1[0]

num1_max = num1[0]
num1_min = num1[1]
if num1[1] > num1_max:
    num1_max = num1[1]
    num1_min = num1[0]



num2_min = num2[0]
num2_max = num2[1]
if num2[1] < num2_min:
    num2_min = num2[1]
    num2_max = num2[0]

mid = int(num1_min) + int(num2_max)

if mid > 9:
    mid %= 10

print(f"{num1_max}{mid}{num2_min}")