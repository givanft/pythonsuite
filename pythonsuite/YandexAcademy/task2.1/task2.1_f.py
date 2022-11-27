product_name = input()
price = int(input())
mass = int(input())
baks = int(input())

total = int(mass * price)

print(f"Chek\n{product_name} - {mass}kg - {price}rub/kg")
print(f"Itogo: {total}rub")
print(f"Vneceno: {baks}rub")
print(f"Sdacha: {baks - total}rub")