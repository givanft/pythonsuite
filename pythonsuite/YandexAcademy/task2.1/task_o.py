h: int = 8
m: int = 0
t: int = 65

#h: int = int(input())
#m: int = int(input())
#t: int = int(input())

t += m

h1 = int(t / 60)
remain = int(t % 60)

h += h1
if h > 23:
    h %= 24

hours: str = str(h)
if h < 10:
    hours = "0" + hours 

minutes: str = str(remain)
if remain < 10:
    minutes = "0" + minutes

print(f"{hours}:{minutes}")
