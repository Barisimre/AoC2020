import math
import numpy

# Add some new lines at the end of the file then this works


required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def lines():
    with open("4.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    p = []
    for a in lines():

        fs = a.split()

        if a == '\n':
            post.append(p.copy())
            p = []
            pass

        for f in fs:
            p.append(f[:f.index(':')])
        

    return post

lines = process_lines()
count = 0
for l in lines:
    for f in required:
        if f not in l:
            count += 1
            break
print(len(lines) - count)

# Solve