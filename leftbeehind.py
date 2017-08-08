import sys

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[:-2]

for item in lines:
    sweet, sour = map(int, item.split())
    if (sweet + sour) == 13:
        print "Never speak again."
    elif sweet > sour:
        print "To the convention."
    elif sour > sweet:
        print "Left beehind."
    else:
        print "Undecided."
