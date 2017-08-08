import sys

input = sys.stdin.read()
line = input.split("\n")
line = line[:-1]

n1 = int(line[0])
n2 = int(line[1])

if (n2 - n1) > 180:
    print (n2 - n1 - 360)
elif (n2 - n1) > -180:
    print (n2 - n1)
else:
    print (n2 - n1 + 360)
