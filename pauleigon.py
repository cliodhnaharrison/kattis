import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]
values = values[0].split()

servers = ["paul", "opponent"]
result = 0
count = 0
i = 0

serves = int(values[1]) + int(values[2])
int_v = int(values[0])

while i <= serves:
	if i % int_v == 0:
		if count % 2 == 0:
			result = 0
		else:
			result = 1
	count += 1
	i += 1

print (servers[result])
		