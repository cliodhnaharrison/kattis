import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
hands, suit = map(str, line[0].split())
plays = line[1:-1]

total = 0

suit_pos = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
suit_neg = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

for item in plays:
    if item[1] == suit:
        total += suit_pos[item[0]]
    else:
        total += suit_neg[item[0]]

print total
