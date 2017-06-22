import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-2]

start_num = int(values[0])
i = 0
dist_time = []

while i < len(values):

	if len(values[i]) <= 2:
		start_num = int(values[i])
		i += 1
		dist_time.append(values[i:i + start_num])
		
	else:
		i += 1
	
totals = []

for item in dist_time:
	total = 0
	current_time = 0
	for vals in item:
		speed, time = map(int, vals.split())
		total += (time - current_time) * int(speed)
		current_time = time
	totals.append(total)

	
for item in totals:
	print (str(item) + " miles")
