### TUPLE - cannot be modified! 'a = ()' => more items are allowed | 'a = tuple()' => only one arg is allowed
tpl1 = tuple("Ivan Gorshenin")
tpl2 = ('Ivan', 12, 1983.2)
tpl3 = 'Ivan', 12, 1983.2

print(tpl1[0])
print(tpl1.__sizeof__())

print(tpl2[0])
print(tpl2.__sizeof__())

print(tpl3[1])
print(tpl3.__sizeof__())