n, p, x, y = map(int, input().split())
time = 0

if n > p:
    print(p * x)
else:
    count = 0
    i = 1
    while count != p:
        if i % n == 0:
            time += y
        else:
            time += x
            count += 1
        i += 1
    if i % n == 0:
        time += y
    print(time)
