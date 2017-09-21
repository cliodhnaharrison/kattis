s = input()
counts = {}
for char in s:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

ans = 0
for c in counts.values():
    if c % 2 != 0:
        ans += 1

if ans - 1 > 0:
    print (ans-1)
else:
    print ("0")
