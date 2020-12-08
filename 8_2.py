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
        if pc >= len(code):
            return True, acc
        if code[pc][0] == 1:
            return False, acc
        code[pc][0] = 1
        if code[pc][1] == 'acc':
            acc += code[pc][2]
        elif code[pc][1] == 'jmp':
            pc += code[pc][2]
            continue
        pc += 1
        
i = 0
while i < len(boot):
    # print(i)
    while boot[i][1] == 'acc':
        i += 1
    if boot[i][1] == 'jmp':
        boot[i][1] = 'nop'
    else:
        boot[i][1] = 'jmp'
    res, acc = run(boot)
    if res:
        print(acc)
    boot = process_lines()
    i += 1