import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

rs = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

#print(json.dumps(rs.json(), indent = 2))
o = rs.json()
for res in o["results"]:
    print(res["trackName"])
"""
import sys
import json

if len(sys.argv) < 3:
    sys.exit("Too few data")

print("hello, ", sys.argv[1:2])
print(len(sys.argv))
"""

"""
#import random
from random import choice
from random import randint

#coin = choice([0, 1])
arr = []
for i in range(10):
    arr.append(randint(-10, 10))
    print(f"{arr[i]}", end = " ")
print()
#print(coin)
"""