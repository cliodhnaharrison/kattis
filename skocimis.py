import sys

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

a = int(line[0])
b = int(line[1])
c = int(line[2])

diff_ab = b - a - 1
diff_bc = c - b - 1

if diff_ab > diff_bc:
    print diff_ab
else:
    print diff_bc
