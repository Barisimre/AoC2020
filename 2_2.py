
import math


class Pass:
    one = 0
    two = 0
    key = None
    word = None



def lines():
    words = []
    with open("2.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words

def process_lines():
    pre = lines()
    post = []

    for a in pre:
        word = Pass()
        a = a.replace('-', ' ')
        nums = [int(s) for s in a.split() if s.isdigit()]
        word.one = nums[0]
        word.two = nums[1]
        word.key = a[a.find(':')-1]
        word.word = a[a.find(':')+2:]
        post.append(word)        
    return post


lines = process_lines()
correct = 0
for w in lines:
    if (w.word[w.one-1] == w.key and w.word[w.two-1] != w.key) or (w.word[w.one-1] != w.key and w.word[w.two-1] == w.key):
        correct += 1
print(correct)

