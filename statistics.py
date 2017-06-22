import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

sets = []

for item in values:
	sets.append(item.split())
	
numbers = []
	
for item in sets:
	item = [int(i) for i in item]
	item = item[1:]
	numbers.append(item)
	
i = 1

for dataset in numbers:
	maximum = max(dataset)
	minimum = min(dataset)
	range = maximum - minimum
	print ("Case " + str(i) + ": " + str(minimum) + " " + str(maximum) + " " + str(range))
	i += 1
	