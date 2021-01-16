n = int(input())

answers = [input() for _ in range(n)]
counter = 0

for i in range(1, len(answers)):
    if answers[i] == answers[i-1]:
        counter += 1

print (counter)
