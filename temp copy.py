import math
import numpy
import re
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
            n = f[:f.index(':')]
            r = f[f.index(':')+1:]

            if n == "byr" and not (int(r) >= 1920 and int(r) <= 2002):
                p.append('~')
            if n == "iyr" and not (int(r) >= 2010 and int(r) <= 2020):
                p.append('~')
            if n == "eyr" and not (int(r) >= 2020 and int(r) <= 2030):
                p.append('~')
            
            if n == "hgt":
                if not(r[-2:] == 'cm' and int(r[:-2]) >= 150 and int(r[:-2]) <= 193):
                    p.append('~')
                if not(r[-2:] == 'in' and int(r[:-2]) >= 59 and int(r[:-2]) <= 76):
                    p.append('~')                
            if n == "hcl":
                regex = re.compile(r'^#[0-9a-f]{6}$')
                if not regex.match(r):
                    p.append('~') 
            if n == "ecl":
                c = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if r not in c:
                    p.append('~') 
            if n == "pid" and len(r) != 9:
                p.append('~') 
            p.append(f[:f.index(':')])

            
    return post

lines = process_lines()
print(len(lines))
count = 0
for l in lines:
    if not '~' in l:
        print(l)
        count += 1
        pass
    for f in required:
        if f not in l:
            count += 1
            break
        
print(len(lines) - count)

# Solve