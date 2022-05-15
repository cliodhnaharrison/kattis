n = int(input())
v = 7

for _ in range(n):
    s = input()
    if "o" in s and v < 10:
            v += 1
    elif "e" in s and v > 0:
            v -= 1

print (v)
