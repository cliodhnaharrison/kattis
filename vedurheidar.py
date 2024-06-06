v = int(input())
n = int(input())
for _ in range(n):
    s, k = input().split()
    if int(k) < v:
        print(s, "lokud")
    else:
        print(s, "opin")
