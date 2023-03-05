# https://open.kattis.com/problems/upprodun

n = int(input())
m = int(input())

if n == 1:
    print("*" * m)
elif n == 2:
    print("*" * (m // 2))
    if m % 2 == 0:
        print("*" * (m // 2))
    else:
        print("*" * ((m // 2) + 1))
elif m % n == 0:
    for _ in range(n):
        print("*" * (m // n))
else:
    r = m % n
    d = m // n
    
    for _ in range(n):
        if r > 0:
            print("*" * (d+1))
            r -= 1
        else:
            print("*" * d)
