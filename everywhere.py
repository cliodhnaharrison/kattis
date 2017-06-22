import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
trips = line.split(" ")

trips = trips[1:-1]
totals = []
i = 0
trip = []

while i < len(trips):
	if trips[i].isnumeric() == False:
		if trips[i] not in trip:
			trip.append(trips[i])
	
	else:
		totals.append(len(trip))
		trip = []
	i += 1
	
totals.append(len(trip))
totals = totals[1:]
for item in totals:
	print (item)
