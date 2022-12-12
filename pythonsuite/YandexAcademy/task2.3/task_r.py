# -* - coding: cp1251 -*-
n: int = 98

root: int = n // 2
first_output: bool = True
symbol_multiple: str = ""

div_n: int = 2
while div_n < root:
    if n % div_n == 0:
        if first_output is False:
            symbol_multiple = " * "

        print(f"{symbol_multiple}{div_n}", end="")
        n /= div_n
        first_output = False
    else:
        div_n += 1