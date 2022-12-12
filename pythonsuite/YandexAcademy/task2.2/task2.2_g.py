n = int(input())
q = str(n // 1000)
c = str(n // 100 % 10)
v = str(n % 10)
m = str(n % 100 // 10)
f = v + m + c + q
if str(n) == f:
    print("YES")
else:
    print("NO")



