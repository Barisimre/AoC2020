import math
import numpy

def lines():
    with open("10.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(int(a.strip()))
    return sorted(post)

lines = process_lines()
lines.append(max(lines)+3)

port = 0
diffs = []
for a in lines:
    if a - port < 4:
        diffs.append(a-port)
        port = a
print(diffs.count(1)*diffs.count(3))

