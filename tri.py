import sys

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

def equation(line):
    line = [int(x) for x in line]
    if line[0] + line[1] == line[2]:
        return str(line[0]) + "+" + str(line[1]) + "=" + str(line[2])

    elif line[0] - line[1] == line[2]:
        return str(line[0]) + "-" + str(line[1]) + "=" + str(line[2])

    elif line[0] / line[1] == line[2]:
        return str(line[0]) + "/" + str(line[1]) + "=" + str(line[2])

    elif line[0] * line[1] == line[2]:
        return str(line[0]) + "*" + str(line[1]) + "=" + str(line[2])

    elif line[1] + line[2] == line[0]:
        return str(line[0]) + "=" + str(line[1]) + "+" + str(line[2])

    elif line[1] - line[2] == line[0]:
        return str(line[0]) + "=" + str(line[1]) + "-" + str(line[2])

    elif line[1] / line[2] == line[0]:
        return str(line[0]) + "=" + str(line[1]) + "/" + str(line[2])

    elif line[1] * line[2] == line[0]:
        return str(line[0]) + "=" + str(line[1]) + "*" + str(line[2])

    else:
        return None

print equation(line)
