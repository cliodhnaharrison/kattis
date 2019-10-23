def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

n = int(input())

for _ in range(n):
    num = int(input())
    s = sum_digits(num)
    for i in range(num, -1, -1):
        if sum_digits(i) == s-1:
            print (i)
            break
