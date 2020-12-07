import math
import numpy

def lines():
    with open("7.txt") as fp:
        return fp.readlines()

stops = set()
def process_lines():
    parents = {}
    for a in lines():
        s = list(a.split(' '))
        if 'no other' in a:
            stops.add(s[0]+s[1])
            continue
        
        parent = s[0]+s[1]

        if parent not in parents:
            parents[parent] = set()
        
        if ',' not in a:
            parents[parent].add((int(s[4]), s[5]+s[6]))
            continue
        else:
            for i in range(len(s)):
                if s[i].isdigit():
                    parents[parent].add((int(s[i]), s[i+1]+s[i+2]))
                i += 1
    return parents


sg = 'shinygold'
parents = process_lines()

count = 0

def get_count(color):

    if color in stops:
        return 1
    res = 0
    for (n, c) in parents[color]:
        res += n*get_count(c)
    return res+1

print(get_count('shinygold')-1)