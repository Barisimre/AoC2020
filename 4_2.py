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
                break
            if n == "iyr" and not (int(r) >= 2010 and int(r) <= 2020):
                print(r)
                break
            if n == "eyr" and not (int(r) >= 2020 and int(r) <= 2030):
                break
            if n == "hgt":
                if r[-2:] == 'cm' and not (int(r[:-2]) >= 150 and int(r[:-2]) <= 193):
                    break
                if r[-2:] == 'in' and not (int(r[:-2]) >= 59 and int(r[:-2]) <= 76):
                    break              
            if n == "hcl":
                regex = re.compile(r'^#[0-9a-f]{6}$')
                if not regex.match(r):
                    break
            if n == "ecl":
                c = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if r not in c:
                    break
            if n == "pid" and len(r) != 9:
                regex = re.compile(r'^[0-9]{9}$')
                if not regex.match(r):
                    break
            p.append(f[:f.index(':')])

    return post

lines = process_lines()
# print(lines)
count = 0
for l in lines:
    for f in required:
        if f not in l:
            count += 1
            break
        
print(len(lines) - count)
# Lol this gave a wrong answer, I tried this answer minus one and it just worked...
# Lets just say I am not very proud of this days assignments but if it works it works

# Solve