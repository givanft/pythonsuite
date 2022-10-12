def get_dict(**args):
    return args

def get_tuple(*args):
    return args

def func(x: int, y: float, z: int = 2) -> float:
    return x * y * z

a: int = 100
b: float = 3.14
print(func(a, b))

print(get_tuple(10, 15.5, 'Ivan'))

print(get_dict(a=10, b=15, name='Ivan'))

add = lambda x, y: x+y
print(add(1,2))

print((lambda x, y: x*y)(5, 10))

