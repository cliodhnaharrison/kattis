n = int(input())
press = [int(input()) for _ in range(n)]
on = 0
timer = 0

for i in range(len(press)):
    on ^= 1
    if i == 0:
        continue
    elif not on:
        timer += (press[i] - press[i-1])

if on:
    print("still running")
else:
    print(timer)
