import sys

input = sys.stdin.read()
line = input.strip("\n")

cards = [line[i:i+3] for i in range(0, len(line), 3)]
H = 0
P = 0
K = 0
T = 0

if len(cards) > len(set(cards)):
    print "GRESKA"
else:
    for item in cards:
        if item[0] == "H":
            H += 1
        elif item[0] == "P":
            P += 1
        elif item[0] == "K":
            K += 1
        else:
            T += 1
    print 13-P, 13-K, 13-H, 13-T
