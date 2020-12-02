
import math

def lines():
    words = []
    with open("1.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words

def process_lines():
    pre = lines()
    post = []
    for a in pre:
        post.append(int(a))
    return post


lines = process_lines()


for x in lines:
    for y in lines:
        if x+y == 2020:
            print(x*y)