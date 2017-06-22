import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")

line = line.split(" ")
line = line[1:-1]
count = 0

for item in line:
	if int(item) < 0:
		count += 1
		
print (count)