import sys

input = sys.stdin.read()
lines = input.split("\n")

start = 0
tests = []
lines = lines[1:-1]

for i in range(len(lines)):
    if lines[i] == "what does the fox say?":
        tests.append(lines[start:i])
        start = i + 1

for case in tests:
    sounds = case[0].split()
    lines = case[1:]
    known = []
    fox = []

    for item in lines:
        sound = item.split()[-1]
        known.append(sound)

    for item in sounds:
        if item not in known:
            fox.append(item)

    print " ".join(fox)
