n = int(input())

for _ in range(n):
    heart = input().split()
    b = int(heart[0])
    p = float(heart[1])

    calculated = (60 * b) / p
    minimum = (60 * (b - 1)) / p
    maximum = (60 * (b + 1)) / p

    print (minimum, calculated, maximum)
