import math
import numpy

def lines():
    words = []
    with open("_.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words

def process_lines():
    pre = lines()
    post = []
    for a in pre:
        pass
    return post

lines = process_lines()
# Solve