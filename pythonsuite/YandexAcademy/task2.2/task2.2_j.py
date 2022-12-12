num: int = int(input())

n3: int = num % 10
num = int(num / 10)

n2: int = num % 10
n1: int = int(num / 10)

f1 = n1 + n2
f2 = n2 + n3

if f1 < f2:
    print(f"{f2}{f1}")
else:
    print(f"{f1}{f2}")