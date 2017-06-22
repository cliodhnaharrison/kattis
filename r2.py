import sys

inputstd = sys.stdin.read()

line = inputstd.strip("\n")
values = line.split(" ")

r1 = int(values[0])
s = int(values[1])

r2 = (s * 2) - r1

print (r2)
