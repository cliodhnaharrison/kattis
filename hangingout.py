m, n = map(int, input().split())

terrace = 0
turn_away = 0

for _ in range(n):
    s = input().split()
    if s[0] == "enter":
        if terrace + int(s[1]) > m:
            turn_away += 1
        else:
            terrace += int(s[1])
    elif s[0] == "leave":
        terrace -= int(s[1])

print (turn_away)
