import sys

input = sys.stdin.read()
line = input.split("\n")
n = line[0]
line = line[1:-1]

for item in line:
    item = item.split()
    if len(item) > 1:
        if item[0] == "simon" and item[1] == "says":
            print " ".join(item[2:])
        else:
            print " "
    else:
        print " "
