import itertools
import sys

dwarves = [int(x) for x in sys.stdin.read().split("\n")[:-1]]

possibilties = list(itertools.combinations(dwarves, 7))
answer = []
for table in possibilties:
    if sum(table) == 100:
        answer = table
        break

for item in answer:
    print item
