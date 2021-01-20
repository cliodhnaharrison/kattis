n = int(input())

numbers = [input() for _ in range(n)][::-1]

for x in numbers:
    print (x)
