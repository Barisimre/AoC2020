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
call = 0

@functools.lru_cache(maxsize=None)
def count(num, l):
    global call
    call += 1
    l = list(l)
    global end
    cs = 0
    p = 1
    if len(l) == 1:
        return 1
    for a in l:
        if a - num < 4:
            cs += count(a, tuple(l[p:])) # something something lists are not hashable something
        p += 1
    return cs

print(count(0, tuple(lines)))
print(call)