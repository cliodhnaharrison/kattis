import sys

inputstd = sys.stdin.read()
line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]
values = values[0].split(" ")

results = []

for die in values:
	result = int(die) + 1
	if result not in results:
		results.append(result)
		
results = sorted(results)
		
if len(results) > 1:
	for i in range(results[0], results[-1]):
		results.append(i)
		
results = sorted(list(set(results)))

for item in results:
	print (item)