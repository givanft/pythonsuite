### DICT: a{} | d = dict() | d = dict.fromkeys([keys], value)
dct1 = {'name':'Ivan', 'surname':'Gorshenin', 'age':39}
dct2 = dict(name='Ivan', surname='Gorshenin', age=39)
dct3 = dict.fromkeys(['name', 'surname', 'age'], "Ivan")

print(dct1)
print(dct1.__sizeof__())

print(dct2)
print(dct2.__sizeof__())

print(dct3)
print(dct3.__sizeof__())