n, m = map(int, input().split())

while n != 0 and m != 0:
    doom = False
    dragons = []
    knights = []
    for _ in range(n):
        d = int(input())
        dragons.append(d)
    for _ in range(m):
        k = int(input())
        knights.append(k)

    dragons = sorted(dragons)
    knights = sorted(knights)
    knights = [k for k in knights if k >= dragons[0]]
    gold = 0

    if max(dragons) > max(knights):
        doom = True
    elif len(dragons) > len(knights):
        doom = True
    else:
        i = -1
        for head in dragons:
            while i < len(knights):
                i += 1
                if i >= len(knights):
                    doom = True
                    break
                if knights[i] >= head:
                    gold += knights[i]
                    break


    if doom:
        print ("Loowater is doomed!")
    else:
        print (gold)
    n, m = map(int, input().split())
