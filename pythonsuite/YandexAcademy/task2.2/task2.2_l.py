n1: int = 1
n2: int = 2
n3: int = 3

output = "NO"

if (n1 < (n2 + n3)) and (n2 < (n1 + n3)) and (n3 < (n1 + n2)):
    output = "YES"

print(output)

