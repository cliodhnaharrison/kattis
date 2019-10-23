hand = map(str, input().split())

strengths = []

for card in hand:
    c = card[0]
    s = 1
    for c2 in hand:
        if c == c2[0]:
            s += 1
    strengths.append(s)

print (max(strengths))
