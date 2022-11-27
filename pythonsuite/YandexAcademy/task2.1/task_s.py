

line_const_len: int = 35

prod_name: str = "chereshnya"
price: int = 2
mass: int = 3
money: int = 10

print("chek".center(line_const_len, '='))

tovar_line1: str = "Tovar:"
tovar_line2: str = f"{prod_name}"
print(f"{tovar_line1}{tovar_line2.rjust(line_const_len - len(tovar_line1),' ')}")

price_line1: str = "Cena:"
price_line2: str = f"{mass}kg * {price}rub/kg"
print(f"{price_line1}{price_line2.rjust(line_const_len - len(price_line1),' ')}")

itogo_line1: str = "Itogo:"
itogo_line2: str = f"{mass * price}rub"
print(f"{itogo_line1}{itogo_line2.rjust(line_const_len - len(itogo_line1),' ')}")

vneceno_line1: str = "Vneceno:"
vneceno_line2: str = f"{money}rub"
print(f"{vneceno_line1}{vneceno_line2.rjust(line_const_len - len(vneceno_line1),' ')}")

sdacha_line1: str = "Sdacha:"
sdacha_line2: str = f"{money - (mass * price)}rub"
print(f"{sdacha_line1}{sdacha_line2.rjust(line_const_len - len(sdacha_line1),' ')}")

print("=".center(line_const_len, '='))

