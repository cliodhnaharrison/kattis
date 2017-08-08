import sys
from itertools import permutations

input = sys.stdin.read()
line = input.strip("\n")

perms = [''.join(p) for p in permutations(line)]
bigger = []

for item in perms:
    if int(item) > int(line):
        bigger.append(int(item))

if len(bigger) > 0:
    print min(bigger)
else:
    print "0"
