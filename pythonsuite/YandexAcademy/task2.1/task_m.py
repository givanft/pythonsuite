n_child: int = 20
n_candy: int = 500

n_candy_for_all: int = int(n_candy / n_child)
n_candy_remain: int = n_candy % n_child

print(f"{n_candy_for_all}")
print(f"{n_candy_remain}")