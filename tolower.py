p, t = map(int, input().split())

count = 0

for _ in range(p):
    tests = []

    for _ in range(t):
        tests.append(input())
    passed = True
    for item in tests:
        if item.lower() != item:
            for char in item[1:]:
                if char.lower() != char:
                    passed = False
                    break
    if passed == True:
        count += 1

print(count)
