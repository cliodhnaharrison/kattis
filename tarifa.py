import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[:-1]

usage = values[2:]
total = 0

for item in usage:
	total += int(values[0]) - int(item)
	
total += int(values[0])

print (total)