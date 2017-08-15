import sys
from math import ceil, log

input = sys.stdin.read()
line = float(input.strip("\n"))

print int(ceil(log(line, 2) + 1))
