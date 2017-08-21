import sys

inputs = sys.stdin.read().split("\n")[:-1]
num_rolls = int(inputs[0])
orig_rolls = [int(x) for x in inputs[1].split()]
rolls = list(orig_rolls)

while len(rolls) != 0:
    set_rolls = set(rolls)
    max_set = max(set_rolls)
    if rolls.count(max_set) > 1:
        rolls[:] = [x for x in rolls if x != max_set]
    else:
        print orig_rolls.index(max_set) + 1
        break

if len(rolls) == 0:
    print "none"
