import math
import numpy

def lines():
    with open("7.txt") as fp:
        return fp.readlines()

def process_lines():
    parents = {}
    for a in lines():
        if 'no other' in a:
            continue
        s = list(a.split(' '))
        parent = s[0]+s[1]

        if parent not in parents:
            parents[parent] = set()
        
        if ',' not in a:
            parents[parent].add(s[5]+s[6])
            continue
        else:
            for i in range(len(s)):
                if s[i].isdigit():
                    parents[parent].add(s[i+1]+s[i+2])
                i += 1
    return parents


sg = 'shinygold'
parents = process_lines()
res = set()
res.add(sg)

num = 0
while len(res) != num:
    num = len(res)

    for k, v in parents.items():
        for i in v:
            if i in res:
                res.add(k)

print(num - 1)