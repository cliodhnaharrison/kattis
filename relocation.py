# https://open.kattis.com/problems/relocation

n, q = map(int, input().split())
companies = {k:int(v) for k,v in zip(range(1, n+1), input().split())}

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        companies[a] = b
    else:
        print(abs(companies[a] - companies[b]))
