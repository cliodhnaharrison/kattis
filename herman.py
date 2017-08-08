import sys
import math

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

r = int(line[0])
pi_taxi = 2.0

area_euc = math.pi * (r**2)
area_taxi = (pi_taxi * (r**2))

print ("{0:.06f}".format(area_euc))
print ("{0:.06f}".format(area_taxi))
