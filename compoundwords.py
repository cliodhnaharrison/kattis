import sys
import itertools
from itertools import permutations

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

compounds = list(itertools.combinations(line, 2))

words = []

for word in compounds:
    words.append([''.join(p) for p in permutations(word)])

flat_list = [item for sublist in words for item in sublist]

for item in sorted(set(flat_list)):
    print item
