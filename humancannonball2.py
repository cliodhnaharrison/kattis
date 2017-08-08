import sys
import math

inputstd = sys.stdin.read()

line = inputstd.split("\n")
N = line[0]
lines = line[1:-1]
g = 9.81


for item in lines:
    v, angle, x1, h1, h2 = map(float, item.split())
    t = x1 / (v * (math.cos(math.radians(angle))))
    y = v * t * (math.sin(math.radians(angle))) - (0.5 * g) * (t ** 2)
    if h1+1 < y < h2-1:
        print "Safe"
    else:
        print "Not Safe"
