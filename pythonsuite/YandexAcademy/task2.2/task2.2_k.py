num: int = 748

n3: int = num % 10
num = int(num / 10)

n2: int = num % 10
n1: int = int(num / 10)

n_min: int = min(n1, n2, n3)
n_max: int = max(n1, n2, n3)

n_sum: int = n_min + n_max

if n_sum == ((n1 + n2 + n3 - n_sum) * 2):
    print("YES")
else:
    print(f"NO")


