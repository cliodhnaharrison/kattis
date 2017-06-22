import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[1:-1]

for item in values:
	print (len(item))