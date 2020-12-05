import math
import numpy

def lines():
    with open("5.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        post.append(a)
    return post

# First 7 makes a binary number
# Last 3 makes a binary number
# first 7 times 8 is just move 3 digits to the left
# So the whole thing is just a binary number

lines = process_lines()

# lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL", "FBFBBFFRLR"]
res = []


for l in lines:
    r = l.replace('F', '0')
    r = r.replace('B', '1')
    r = r.replace('L', '0')
    r = r.replace('R', '1')

    res.append(int(r, 2))
print(max(res))
        
