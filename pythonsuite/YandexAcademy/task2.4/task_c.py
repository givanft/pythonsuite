n: int = int(input())

n_len: int = 1
n_tmp: int = n_len

for i in range(1, n + 1):
    print(f"{i} ", end="")
    if (n_len := n_len - 1) == 0:
        n_tmp += 1
        n_len = n_tmp
        print()
        
    
#for i in range(1, n + 1):
#    for j in range(1, n + 1):
#        print(f"{i} * {j} = {i * j}")
