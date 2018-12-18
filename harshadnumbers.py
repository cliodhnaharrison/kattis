n = input()

sum_digits = sum([int(x) for x in list(n)])

n = int(n)

while True:
    if n % sum_digits == 0:
        break
    else:
        n += 1
        sum_digits = sum([int(x) for x in list(str(n))])

print (n)
