w = int(input())
n = int(input())
area = 0

for _ in range(n):
    m, l = map(int, input().split())
    area += m*l
    
print(int(area/w))
