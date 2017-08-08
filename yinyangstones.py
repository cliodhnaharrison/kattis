import sys

line = sys.stdin.read()
line = line.strip("\n")

num_w = line.count("W")
num_b = line.count("B")

if num_w == num_b:
    print "1"
else:
    print "0"
