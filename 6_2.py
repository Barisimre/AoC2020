import math
import numpy

# Add some lines to the end of the input


def lines():
    with open("6.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    count = 0
    t = ""
    for a in lines():
        if a == '\n':
            post.append((count, t))
            count = 0
            t = ""
        else:
            count += 1
            t += a.strip()
        
    return post

lines = process_lines()

total = 0

for (c, l) in lines:
    sub  = 0
    qs = []
    for q in l:
        if l.count(q) == c and q not in qs:
            sub += 1
            qs.append(q)
    total += sub
print(total)
