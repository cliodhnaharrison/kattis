import sys

input = sys.stdin.read()
line = input.split("\n")
n = line[0]
line = line[1:-1]

entered = []

for door in line:
    door = door.split()
    if door[0] == "entry":
        if door[1] not in entered:
            entered.append(door[1])
            print door[1], "entered"
        else:
            print door[1], "entered (ANOMALY)"
    else:
        if door[1] in entered:
            entered.remove(door[1])
            print door[1], "exited"
        else:
            print door[1], "exited (ANOMALY)"
