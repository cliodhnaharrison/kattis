import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[:-2]


def easy(number):
    n = int(number)
    for i in range(11, 100000):
        m = int(i)
        multiple = str(n * m)
        multi_total = 0
        n_total = 0
        for item in multiple:
            multi_total += int(item)
        for item in str(n):
            n_total += int(item)
        if n_total == multi_total:
            return m
        else:
            continue

for item in values:
    print easy(item)
