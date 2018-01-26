import itertools

n = int(input())
answer = 0

if n < 2:
    print (answer)
elif n == 2:
    print ("1")
else:
    answer = 4
    i = 3
    add = 7
    add2 = 8
    while i != n:
        answer += add
        add += add2
        add2 *= 2
        i += 1
    print (answer)
