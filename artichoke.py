from math import sin
from math import cos 

p, a, b, c, d, n = map(int, input().split())

dif = 0.0
max_num = p * (sin(a + b) + cos(c + d) + 2)
i = 2
while i <= n:
    value = p * (sin(a * i + b) + cos(c * i + d) + 2)
    if max_num < value:
        max_num = value
    elif max_num - value > dif:
        dif = max_num - value
    i += 1

print (dif)
