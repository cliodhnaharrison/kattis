import sys

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()
phrase = line[0]
password = line[1]

i = 0


for char in password:
    if char == phrase[i]:
        i += 1
        if i >= len(phrase):
            break
        continue
    if char in phrase[i:]:
        break


if i == len(phrase):
    print("PASS")
else:
    print("FAIL")
