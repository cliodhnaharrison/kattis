import sys

inputstd = sys.stdin.read()

line = inputstd.strip("\n")
n = int(line)

if n % 2 == 0:
	print ("Bob")
else:
	print ("Alice")