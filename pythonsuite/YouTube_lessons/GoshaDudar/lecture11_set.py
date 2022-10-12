### SET: duplicates are not allowed! sst = set() | sst = {a1, a2, a3} | sst = frozenset() => only one arg is allowed
sst1 = set("hello")
sst2 = {1,2,3}
sst3 = frozenset("frozen")

sst1.add(12)
sst1.add(12)
sst1.add(21)

print(sst1)
print(type(sst1))
print(sst1.__sizeof__())

print(sst2)
print(type(sst2))
print(sst2.__sizeof__())

print(sst3)
print(type(sst3))
print(sst3.__sizeof__())

sst4 = ['r','d','r','d']
print(sst4)
print(set(sst4))
print(type(sst4))
print(sst4.__sizeof__())

