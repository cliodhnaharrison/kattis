p, n = map(int, input().split())

parts = []
answer = "paradox avoided"

for i in range(n):
    part = input()
    if part not in parts:
        parts.append(part)
    if len(parts) == p:
        answer = str(i + 1)
        parts.append("done")

print (answer)
