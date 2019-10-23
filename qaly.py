n = int(input())
answer = 0

for _ in range(n):
    q, y = map(float, input().split())
    answer += q*y

print (answer)
