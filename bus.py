t = int(input())

for _ in range(t):
    n = int(input())
    k = 0
    while n > 0:
        k += 0.5
        k = k * 2
        n -= 1
    print (int(k))
