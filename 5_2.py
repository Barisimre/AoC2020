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

lines = process_lines()

# lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL", "FBFBBFFRLR"]
res = []

for l in lines:
    r = l.replace('F', '0')
    r = r.replace('B', '1')
    r = r.replace('L', '0')
    r = r.replace('R', '1')

    res.append(int(r, 2))

# I did this to test the front and back thing expecting like 20 prints, just gave me one lol
for a in range(1025):
    if (a-1) in res and (a+1) in res:
        if a not in res:
            print(a)


        
