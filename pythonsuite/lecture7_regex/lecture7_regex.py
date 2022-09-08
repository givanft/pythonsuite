"""
.       any character except a new line
*       0 or more repetitions
+       1 or more repetitions
?       0 or 1 repetition
{m}     m repetitions
{m, n}  m-n repetitions
^       matches the start of the string
$       matches the end of the string or just before the newline at the end of the string
[]      set of characters
[^]     complementing the set
\d      decimal digit
\D      not a decimal digit
\s      whitespace characters
\S      not a whitespace character
\w      word character, as well as numbers and the underscore (like [a-zA-Z0-9_])
\W      not a word character
A|B     either A or B
(...)   a group
(?:...) non-capturing version
"""

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

#import re
#
#name = input("What's your name? ").strip()
#if matches := re.search(r"^(.+), *(.+)$", name):
#    name = matches.group(2) + " " + matches.group(1)
#print(f"hello, {name}")

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#    print("Valid")
#else:
#    print("Invalid")