import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
N = line[0]
lines = line[1:-1]

for sequence in lines:
    sequence = sequence.split()
    before = sequence[0]
    imports = 0
    for i in range(len(sequence)):
        if int(sequence[i]) > 2 * int(before):
            imports += int(sequence[i]) - (2 * int(before))
        before = sequence[i]

    print imports
