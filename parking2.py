n = int(input())

for _ in range(n):
    t = int(input())
    tests = input().split()
    tests = [int(x) for x in tests]
    dist = max(tests) - min(tests)
    print (dist * 2)
