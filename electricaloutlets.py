# https://open.kattis.com/problems/electricaloutlets

n = int(input())

for _ in range(n):
    power = [int(x) for x in input().split()]
    k = power[0]
    if k == 1:
        print(power[1])
        continue
    power = power[1:]
    power = [x - 1 for x in power]
    power[-1] += 1
    print(sum(power))
        
