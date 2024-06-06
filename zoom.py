n, k = map(int, input().split())
data = [int(x) for x in input().split()]

answer = [str(data[x]) for x in range(k-1, n, k)]
print(" ".join(answer))
