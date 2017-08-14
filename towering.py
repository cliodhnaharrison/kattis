import sys
import itertools

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

heights = [int(x) for x in line[:-2]]
height_tower_one = int(line[-2])
height_tower_two = int(line[-1])

for per in list(itertools.combinations(heights, 3)):
    if sum(per) == height_tower_one:
        tower_one = per
    elif sum(per) == height_tower_two:
        tower_two = per

print " ".join([str(x) for x in sorted(tower_one)][::-1]), " ".join([str(x) for x in sorted(tower_two)][::-1])
