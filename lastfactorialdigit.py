from math import factorial

n = int(input())

for _ in range(n):
    i = int(input())
    fac = str(factorial(i))
    print (fac[-1])
