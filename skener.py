import sys

input = sys.stdin.read()
lines = input.split("\n")
r, c, zr, zc = map(int, lines[0].split())
lines = lines[1:-1]

output = []

for item in lines:
    new_string = ""
    for char in item:
        new_string += char*zc
    output.append(new_string)

for item in output:
    i = 0
    while i < zr:
        print item
        i += 1
