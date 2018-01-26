n, b, h, w = map(int, input().split())

results = []

for _ in range(h):
    price = int(input())
    weekends = [int(x) for x in input().split()]
    for wk in weekends:
        if wk >= n:
            results.append(n*price)

if len(results) == 0 or min(results) > b:
    print ("stay home")
else:
    print (min(results))
