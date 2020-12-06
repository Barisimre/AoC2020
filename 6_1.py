import math
import numpy

# Add some lines to the end of the input


def lines():
    with open("6.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    c = ""
    for a in lines():
        if a == '\n':
            post.append(c)
            c = ""
        else:
            c += a.strip()
        
    return post

lines = process_lines()
sets = []
for l in lines:
    s = set(l)
    sets.append(s)
total = 0
print(sets)
for s in sets:
    total += len(s)
print(total)
