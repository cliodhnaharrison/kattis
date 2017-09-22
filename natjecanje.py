n, s, r = map(int, input().split())
no_canoes = [int(x) for x in input().split()]
extra = [int(x) for x in input().split()]

starting = []
invalid = 0
for value in extra:
    starting.append(value)

for canoe in no_canoes:
    if canoe - 1 in extra:
        starting.append(canoe)
        extra.remove(canoe - 1)
    elif canoe + 1 in extra:
        starting.append(canoe)
        extra.remove(canoe + 1)
    else:
        invalid += 1

print (invalid)
