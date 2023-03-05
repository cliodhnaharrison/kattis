n = int(input())
results = []

for i in range(n):
    costs = [int(x) for x in input().split()]
    for j in range(len(costs)):
        if costs[j] != -1:
            results.append([i+1, j+1, costs[j]])
            
print(len(results))
for x in results:
    print(x[0], x[1], x[2]
