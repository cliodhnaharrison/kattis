x = int(input())
y = int(input())

ans = 0

if x < 0:
    if y < 0:
        ans = 3
    else:
        ans = 2
else:
    if y < 0:
        ans = 4
    else:
        ans = 1

print (ans)
