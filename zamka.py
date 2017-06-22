import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]
l = int(values[0])
d = int(values[1])
x = int(values[2])

target = []

for i in range(l, d+1):
	if i < 10:
		if int(i) == x:
			target.append(int(i))
	else:
		split_i = [int(j) for j in list(str(i))]
		
		if sum(split_i) == x:
			target.append(int(i))
			

print (min(target))
print (max(target))