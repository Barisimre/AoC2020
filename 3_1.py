import math

def lines():
    words = []
    with open("3.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words

def process_lines():
    pre = lines()
    post = []
    for a in pre:
        post.append(list(a)[:-1]) # That [:-1] took me 10 minutes :(
    return post


lines = process_lines()
print(lines)
hor = 0
ver = 0

tree = 0

while ver < len(lines):
    # print(lines[ver][hor])
    if lines[ver][hor] == "#":
        tree += 1
    ver += 1
    hor += 3
    hor = hor % len(lines[0])
print(tree)

