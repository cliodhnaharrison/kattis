import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
line = line.split(" ")
print (line[1])