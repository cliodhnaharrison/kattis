n = int(input())

results = []

for _ in range(n):
    m, d = map(int, input().split())\

    result = sum(range(d + 1)) + d

    results.append((m, result))

for i in results:
    print (i[0], i[1])
