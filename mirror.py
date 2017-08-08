import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
N = line[0]
lines = line[1:-1]

count = 0
strings = []
results = []

for line in lines:
    line = line.replace(" ", "")
    if count <= N:
        if line.isalnum() == True and count != 0:
            results.append("Test " + str(count))
            for item in strings[::-1]:
                results.append(item[::-1])
                strings = []
            count += 1
        elif line.isalnum() == True:
            count += 1
        else:
            strings.append(line)
    else:
        break

results.append("Test " + str(count))
for item in strings[::-1]:
    results.append(item[::-1])

for item in results:
    print item
