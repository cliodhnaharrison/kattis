import sys

input = sys.stdin.read()
line = input.split("\n")
line = line[:-1]

for item in line:
    a, b, s, m, n = map(int, item.split())
    print a, b, s, m, n
