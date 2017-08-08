import sys
import string

input = sys.stdin.read()
line = input.split("\n")
n = line[0]
line = line[1:-1]

if sorted(line) == line:
    print "INCREASING"
elif line == sorted(line)[::-1]:
    print "DECREASING"
else:
    print "NEITHER"
