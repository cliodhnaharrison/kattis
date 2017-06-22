import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n"," ")
line = line.split(" ")
line = line[1:-1]


for n in line:
	if int(n) % 2 == 0:
		print (str(n) + " is even")
	else:
		print (str(n) + " is odd")