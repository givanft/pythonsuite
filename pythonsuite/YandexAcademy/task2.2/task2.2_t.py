# -*- coding: cp1251 -*-

s1: str = input()
s2: str = input()
s3: str = input()

s1 = "зайка лопух"#"березка елочка зайка волк березка"
s2 = "березка зайка"#"сосна сосна сосна елочка грибочки медведь"
s3 = "березка елочка березка"#"сосна сосна сосна белочка сосна белочка"

l1: int = 0
l2: int = 0
l3: int = 0

z: str = "зайка"

if z in s1:
    l1 = len(s1)

if z in s2:
    l2 = len(s2)

if z in s3:
    l3 = len(s3)

output: str = ""

if l1 > 0 and l2 > 0 and l3 > 0:
    output = min(s1, s2, s3)
elif l1 > 0 and l2 > 0:
    output = min(s1, s2)
elif l1 > 0 and l3 > 0:
    output = min(s1, s3)
elif l2 > 0 and l3 > 0:
    output = min(s2, s3)
elif l1 > 0:
    output = s1
elif l2 > 0:
    output = s2
elif l3 > 0:
    output = s3

print(f"{output} {len(output)}")



#if l1 > 0 and l2 > 0 and l3 > 0:
#    k = min(s1, s2, s3)


#elif l1 > 0 and l2 > 0:
#    print(f"{min(s1, s2)} {min(l1, l2)}")
#elif l1 > 0 and l3 > 0:
#    print(f"{min(s1, s3)} {min(l1, l3)}")
#elif l2 > 0 and l3 > 0:
#    print(f"{min(s2, s3)} {min(l2, l3)}")
#elif l1 > 0:
#    print(f"{s1} {l1}")
#elif l2 > 0:
#    print(f"{s2} {l2}")
#elif l3 > 0:
#    print(f"{s3} {l3}")

#    print(f"{k} {len(k)}")