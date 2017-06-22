import sys

inputstd = sys.stdin.read()

correct = [1, 1, 2, 2, 2, 8]

line = inputstd.strip("\n")
values = line.split(" ")

i = 0
correction = ""

for item in values:
	item = int(item)
	correction += str((correct[i] - item)) + " "
	i += 1
	
print (correction)
	