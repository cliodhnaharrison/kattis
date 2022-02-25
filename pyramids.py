n = int(input()) - 1
side = 1
height = 1

while ((side + 2) ** 2) <= n:
    height += 1
    side += 2
    n -= side ** 2

print(height)
