n = int(input())

for _ in range(n):
    line = input().split()
    p = int(line[1].split("/")[0])
    q = int(line[1].split("/")[1])
    tree = []
    while (p > 1 or q > 1):
        if p > q:
            tree.append("1")
            p -= q
        else:
            tree.append("0")
            q -= p
    tree.append("1")

    print (line[0], int(''.join(tree[::-1]), base=2))
