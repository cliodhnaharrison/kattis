import sys

inputstd = sys.stdin.read()
line = inputstd.split("\n")
line = line[:-1]

cost = float(line[0])
num_lawns = line[1]

total = 0

for item in line[2:]:
	item = item.split(" ")
	total += float(item[0]) * float(item[1])

result = total * cost

print("{0:.7f}".format(round(result,7)))
