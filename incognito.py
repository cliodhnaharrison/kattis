t = int(input())

for _ in range(t):
    n = int(input())
    disguises = {}
    for _ in range(n):
        item, area = map(str, input().split())
        if area in disguises:
            disguises[area].append(item)
        else:
            disguises[area] = [item]
    disguise_lst = list(disguises.values())
    count = 1
    i = 0
    disguise_lst = [len(item) for item in disguise_lst]
    while i <= len(disguise_lst) - 1:
        count += count * disguise_lst[i]
        i += 1
    print (count - 1)
