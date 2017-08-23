import math

d, v = map(int, input().split())

while v != 0:
    print (round(pow((pow(d, 3) * math.pi / 6 - v) / (math.pi / 6), 1.0/3), 9))
    d, v = map(int, input().split())
