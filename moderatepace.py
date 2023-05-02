from statistics import median

n = int(input())
me = [int(x) for x in input().split()]
first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

result = [str(median([me[i], first[i], second[i]])) for i in range(n)]

print(" ".join(result))
