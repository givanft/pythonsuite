n_mass: int = 32
m_price: int = 285
price_part1: int = 300
price_part2: int = 240

total: int = n_mass * m_price
diff_total: int = (n_mass * price_part1) - total
diff_price: int = price_part1 - price_part2

factor: int = int(diff_total / diff_price)

part2_mass: int = factor
part1_mass: int = n_mass - part2_mass

print(f"{part1_mass} {part2_mass}")

