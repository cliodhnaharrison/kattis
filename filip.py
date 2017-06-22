import sys

inputstd = sys.stdin.read()
line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]
values = values[0].split(" ")

numbers = []

for item in values:
	item = item[::-1]
	numbers.append(int(item))
	
print (max(numbers))