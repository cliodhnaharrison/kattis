import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
line = line[1:-1]

cups = {}

for item in line:
    cup = item.split()
    if cup[0].isalpha() == True:
        colour = cup[0]
        radius = float(cup[1])
    else:
        colour = cup[1]
        radius = float(cup[0]) / 2
    cups[colour] = radius

sorted_cups = sorted(cups.items(), key=lambda x: (-x[1], x[0]))

list_cups = []
for cup in sorted_cups:
     list_cups.append(cup[0])

for item in list_cups[::-1]:
    print item
