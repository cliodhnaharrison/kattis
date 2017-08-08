import sys
from datetime import datetime

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[:-1]

for item in lines:
    item = item.split()
    if len(item[-2]) < 5:
        item[-2] = "0" + item[-2]
    if len(item[-1]) < 5:
        item[-1] = "0" + item[-1]
    a = datetime.strptime(item[-2], "%H:%M")
    b = datetime.strptime(item[-1], "%H:%M")

    answer = str(b - a)
    h, m, s= map(int, answer.split(":"))
    print item[0], item[1], item[2], h, "hours", m, "minutes"
