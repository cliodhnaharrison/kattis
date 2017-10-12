n = int(input())

for _ in range(n):
    l = [int(x) for x in input().split()]
    m = l[0]
    l = l[1:]
    king = 0
    for i in range(1, m - 1):
        prev = l[i-1]
        curr = l[i]
        if curr - prev != 1:
            king = curr
            break
    print (l.index(king) + 1)
