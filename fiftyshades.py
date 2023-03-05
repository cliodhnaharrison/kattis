n = int(input())
ans = 0

for _ in range(n):
    colour = input().lower()
    if "pink" in colour or "rose" in colour:
        ans += 1

if ans > 0:
    print(ans)
else:
    print("I must watch Star Wars with my daughter")
