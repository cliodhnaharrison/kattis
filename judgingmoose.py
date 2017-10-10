import sys

inputs = sys.stdin.read()

n, m = map(int, inputs.split())

if n == 0 and m == 0:
    print "Not a moose"
elif n == m:
    print "Even", n+m
elif n != m:
    print "Odd", max(n, m) * 2
