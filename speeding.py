n = int(input())
prev_dist = 0
prev_time = 0
max_speed = 0

for _ in range(n):
    t, d = map(int, input().split())
    if t == 0:
        continue
    speed = (d - prev_dist) // (t - prev_time)
    if speed > max_speed:
        max_speed = speed
    prev_dist = d
    prev_time = t

print(max_speed)
