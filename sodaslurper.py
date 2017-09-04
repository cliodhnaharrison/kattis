e, f, c = map(int, input().split())

empty = e + f
total = 0
while empty >= c:
    empty -= c
    total += 1
    empty += 1
print (total)
