import math
import numpy

def lines():
    with open("9.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(int(a.strip()))
    return post

def calc(n, l):
    for a in l:
        if (n-a) in l and (n-a) != a:
            return True
    return False


lines = process_lines()

pre_len = 25
i = pre_len
for _ in range(len(lines)):
    buf = lines[i-pre_len:i]
    if not calc(lines[i], buf):
        print(lines[i])
        break
    i += 1






