import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "")

end_str = "PER" * (len(line) / 3)
days = 0

for i in range(len(line)):
    if end_str[i] != line[i]:
        days += 1
    else:
        continue

print days
