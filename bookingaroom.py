import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

rooms_booked = values[0].split()
rooms_available = []
rooms = values[1:]

if rooms_booked[0] == rooms_booked[1]:
	print ("too late")
else:
	i = 1
	while i <= int(rooms_booked[0]):
		if str(i) not in rooms:
			rooms_available.append(i)
		i += 1
	print (rooms_available[0])