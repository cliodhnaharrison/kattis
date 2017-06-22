import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

for item in values:
	num1, num2 = map(int, item.split())
	total = abs(num2 - num1)
	print (total)