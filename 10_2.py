import math
import numpy
from tqdm import tqdm
import functools

def lines():
    with open("10.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(int(a.strip()))
    return sorted(post)
lines = process_lines()
end = max(lines)+3
lines.append(end)

@functools.lru_cache(maxsize=None)
def count(num, l):
    l = list(l)
    global end
    cs = 0
    p = 1
    if len(l) == 1:
        return 1
    for a in l:
        if a - num < 4:
            cs += count(a, tuple(l[p:])) # something something lists are not hashale something
        p += 1
    return cs

print(count(0, tuple(lines)))