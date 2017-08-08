import sys

input = sys.stdin.read()
line = input.split("\n")
n = line[0]
line = line[1:-1]

for item in line:
    item = item.split()
    if item[0] == "Simon" and item[1] == "says":
        print " ".join(item[2:])
    else:
        continue
