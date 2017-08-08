import sys

line = sys.stdin.read()
line = line.split("\n")
n = line[0]
line = line[1:-1][0].split()
line = [int(x) for x in sorted(line)]

output = []
link = []
next = False

for i in range(len(line)):
    if i < len(line) - 1:
        if line[i] + 1 == line[i+1]:
            link.append(line[i])
        else:
            if len(link) > 2:
                link.append(line[i])
                output.append(str(link[0]) + "-" + str(link[-1]))
                link = []
            else:
                for item in link:
                    output.append(item)
                link = []
    else:
        if len(link) > 0:
            output.append(str(link[0]) + "-" + str(link[-1]))
            link = []
        else:
            output.append(line[i])

for item in output:
    print item
