import sys
import math

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

num_matches, width, height = map(int, values[0].split())

matches = values[1:]
diagonal = math.sqrt(height**2 + width**2)

for item in matches:
	if int(item) <= diagonal:
		print ("DA")
		
	else:
		print("NE")