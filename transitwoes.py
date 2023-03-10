# https://open.kattis.com/problems/transitwoes

s, t, n = map(int, input().split())
d = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

i = 0
s += d[0]
d = d[1:]

while s != t:
    if i > len(c) - 1:
      break
    if s % c[i] == 0 or s == c[i]:
      s += b[i]
    elif s > c[i]:
      s += (c[i] * ((s // c[i]) + 1)) - s
      s += b[i]
    elif s < c[i]:
      s += (c[i] - s)
      s += b[i]

    s += d[i]
    i += 1
    
if s > t:
    print("no")
else:
    print("yes")
    
