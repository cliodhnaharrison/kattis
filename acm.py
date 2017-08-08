import sys

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[:-2]

solved = []

for item in lines:
    item = item.split()
    if item[-1] == "right":
        solved.append(item[1])

score = 0

for item in lines:
    item = item.split()
    if item[-1] == "wrong":
        if item[1] in solved:
            score += 20
    else:
        score += int(item[0])

print len(solved), score
