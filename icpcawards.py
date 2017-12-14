n = int(input())

unis = []
winners = []

for _ in range(n):
    while len(winners) < 12:
        s = input()
        spl = s.split()
        if spl[0] not in unis:
            unis.append(spl[0])
            winners.append(s)


for w in winners:
    print (w)
