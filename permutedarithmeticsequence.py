import sys
import itertools

input = sys.stdin.read()
lines = input.split("\n")
num_cases = lines[0]
cases = lines[1:-1]


def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
             return False
    return True

for case in cases:
    case = case.split()
    num_elems = case[0]
    case = [int(x) for x in case[1:]]
    if is_arithmetic(case) == True:
        print "arithmetic"
    elif is_arithmetic(sorted(case)) == True:
        print "permuted arithmetic"
    else:
        print "non-arithmetic"
