import sys

line = sys.stdin.read()
line = line.split("\n")
n, max_time = map(int, line[0].split())
tasks = line[1].split()

total = 0
count = 0

if sum([int(x) for x in tasks]) <= max_time:
    print len(tasks)
    sys.exit()



for item in tasks:
    item = int(item)
    if (total + item) <= max_time:
        total += item
        count += 1
    else:
        break

print count
