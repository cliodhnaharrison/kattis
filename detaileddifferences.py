import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[:-1]

compare = values[1::2]
compare_to = values[0::2]
compare_to = compare_to[1:]

results = []

for i in range(int(values[0])):
    strings = [compare[i], compare_to[i]]
    result = ""
    for j in range(len(compare[i])):
        if compare[i][j] == compare_to[i][j]:
            result += "."
        else:
            result += "*"
    strings.append(result)
    results.append(strings)

for item in results:
    for thing in item:
        print thing
