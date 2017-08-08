import sys

input = sys.stdin.read()
lines = input.split("\n")

sounds = lines[1].split()
lines = lines[2:-2]
known = []
fox = []

for item in lines:
    sound = item.split()[-1]
    known.append(sound)

for item in sounds:
    if item not in known:
        fox.append(item)

print " ".join(fox)
