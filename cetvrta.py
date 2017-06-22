import sys

inputstd = sys.stdin.read()
line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

points = []

for item in values:
	item = item.split()
	points.append(item)
	
xs = []
ys = []

for item in points:
	xs.append(item[0])
	ys.append(item[1])
	
result = ""

if xs.count(xs[0]) == 1:
	result += xs[0] + " "
else:
	if xs[0] != xs[1]:
		result += xs[1] + " "
	else:
		result += xs[2] + " "
	

if ys.count(ys[0]) == 1:
	result += ys[0]
else:
	if ys[0] != ys[1]:
		result += ys[1]
	else:
		result += ys[2]
		
print (result)