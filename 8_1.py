import math
import numpy

def lines():
    with open("8.txt") as fp:
        return fp.readlines()

def process_lines():
    post = []
    for a in lines():
        com, val = a.split(' ')
        post.append([0, com, int(val)])
    return post

boot = process_lines()



def run(code):
    acc = 0
    pc = 0
    while True:
        if code[pc][0] == 1:
            return "repeat", acc
        code[pc][0] = 1
        if code[pc][1] == 'acc':
            acc += code[pc][2]
        elif code[pc][1] == 'jmp':
            pc += code[pc][2]
            continue
        pc += 1
        
print(run(boot))