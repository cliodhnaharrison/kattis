import datetime
from datetime import datetime as dt

n = int(input())

for _ in range(n):
    line = input()
    line = line.split()
    if len(line[-1]) == 1:
        line[-1] = "0" + line[-1]
    if len(line[-2]) == 1:
        line[-2] = "0" + line[-2]

    time_now = line[-2] + line[-1]

    time_now = dt.strptime(time_now, '%H%M')
    minutes = int(line[1])

    if line[0] == "B":
        time_now = time_now - datetime.timedelta(minutes = minutes)
        time_now = str(time_now).split()[1].split(":")
        if time_now[0][0] == "0":
            time_now[0] = time_now[0][1]
        if time_now[1][0] == "0":
            time_now[1] = time_now[1][1]
        print (time_now[0], time_now[1])
    else:
        time_now = time_now + datetime.timedelta(minutes = minutes)
        time_now = str(time_now).split()[1].split(":")
        if time_now[0][0] == "0":
            time_now[0] = time_now[0][1]
        if time_now[1][0] == "0":
            time_now[1] = time_now[1][1]
        print (time_now[0], time_now[1])
