articles, impact = map(int, input().split())

num_scientists = (articles * (impact - 1)) + 1

print (num_scientists)