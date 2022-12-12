n1: int = 23
n2: int = 13
n3: int = 63

d1_2: int = int(n1 % 10)
d1_1: int = int(int(n1 / 10) % 10)

output: str = "_"

if (d1_2 == int(n2 % 10)) and (d1_2 == int(n3 % 10)):
    output = str(d1_2)

if (d1_1 == int(n2 / 10)) and (d1_1 == int(n3 / 10)):
    output = str(d1_1)

print(output)