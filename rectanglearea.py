# https://open.kattis.com/problems/rectanglearea

x1, y1, x2, y2 = map(float, input().split())

l = x1 - (x2)
h = y1 - (y2)
print(round(abs(l)*abs(h), 3))
