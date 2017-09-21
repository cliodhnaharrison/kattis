k = int(input())
n = int(input())

turns = []

for _ in range(n):
    turns.append(input())

total_time = 0
bomb = 210
answer = k

for t in turns:
    time, a = t.split()
    total_time += int(time)
    if total_time > bomb:
        answer = k
        break
    if a == "T":
        k += 1
        if k > 8:
            k = 1

print (answer)
