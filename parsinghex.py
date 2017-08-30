import sys

inputs = sys.stdin.read().split("\n")[:-1]

hexes = []
valids = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

for item in inputs:
    for i in range(len(item)):
        if item[i] == "0":
            if i != len(item) - 1:
                if item[i+1].lower() == "x":
                    hexes.append(item[i:])

for item in hexes:
    hexnum = item[:2]
    new = item[2:]
    for i in range(len(new)):
        if new[i] in valids:
            hexnum += new[i]
        else:
            break
    print hexnum, int(hexnum, 16)
