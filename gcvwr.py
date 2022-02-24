G, T, N = map(int, input().split())
items = sum([int(x) for x in input().split()])

print(int(((G - T) * 0.9) - items))
