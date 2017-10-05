n = int(input())
wins = 0

for _ in range(n):
    attack = input()
    if "CD" not in attack:
        wins += 1

print (wins)
