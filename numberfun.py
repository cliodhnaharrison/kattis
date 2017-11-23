n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    comb = False
    if a + b == c:
        comb = True
    elif a - b == c:
        comb = True
    elif b - a == c:
        comb = True
    elif a * b == c:
        comb = True
    elif a / b == c:
        comb = True
    elif b / a == c:
        comb = True

    if comb:
        print ("Possible")
    else:
        print ("Impossible")
