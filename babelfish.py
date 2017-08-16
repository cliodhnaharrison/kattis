import sys

inputs = sys.stdin.readlines()

d = {}
i = 0

while inputs[i] != "\n":
    words = inputs[i].split()
    d[words[1]] = words[0]
    i += 1


i += 1

while i < len(inputs):
    word = inputs[i].strip()
    print (d[word] if word in d else 'eh')
    i += 1
