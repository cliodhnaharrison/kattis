from functools import reduce
import operator
import math
import sys

s = sys.stdin.read().split("\n")[:-1]

string_counts = []

for string in s:
    counts = []
    seen = []
    for char in string:
        if char not in seen:
            seen.append(char)
            counts.append(string.count(char))
    string_counts.append(counts)

for c in string_counts:
    print (int(math.factorial(sum(c))) // int(reduce(operator.mul, map(math.factorial, c), 1)))
