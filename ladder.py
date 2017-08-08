import sys
import math

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[:-1]

h = int(values[0])
v = int(values[1])

sine = math.sin(math.radians(v))
x = h / sine

print int(math.ceil(x))
