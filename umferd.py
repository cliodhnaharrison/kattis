m = int(input())
n = int(input())
free = 0

for _ in range(n):
    free += input().count(".")
    
print(free / (n*m))
