s = input()

zoom = len(s)
x = 0
y = 0

for i in range(zoom):
    quad = int(s[zoom - i -1])
    if quad != 0:
        if quad == 1:
            x += (2 ** (i+1) // 2)
        elif quad == 2:
            y += (2 ** (i+1) // 2)
        elif quad == 3:
            x += (2 ** (i + 1) // 2)
            y += (2 ** (i + 1) // 2)

print(zoom, x, y)
