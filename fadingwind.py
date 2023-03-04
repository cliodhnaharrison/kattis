from math import floor
h, k, v, s = map(int, input().split())

d = 0

while h > 0:
  v += s 
  v -= max(1, floor(v/10))

  if v >= k:
    h += 1

  if (v > 0) and (v < k):
    h -= 1

  if h == 0:
    v = 0

  if v <= 0:
    h = 0
    v = 0

  d += v

  if s > 0:
    s -= 1

print(d)
