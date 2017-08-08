import sys
import math

line = sys.stdin.read()
line = line.strip("\n")
line = line.split()

b, k, g = map(int, line)

num_groups = k / g
days = (b - 1) / float(num_groups)

print int(math.ceil(days))
