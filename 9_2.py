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
num = 0
for _ in range(len(lines)):
    buf = lines[i-pre_len:i]
    if not calc(lines[i], buf):
        print(lines[i])
        num = lines[i]
        break
    i += 1


for i in range(len(lines)):
    c = 2
    while i+c < len(lines):
        if sum(lines[i:i+c]) == num:
            l = lines[i:i+c]
            print(max(l)+min(l))
            break
        c +=1



