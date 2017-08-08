import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
n = line[0]
line = line[1:-1]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]

for sentence in line:
    sentence = sentence.lower()
    missing = []
    for letter in alphabet:
        if letter not in sentence:
            missing.append(letter)

    if len(missing) == 0:
        print "pangram"
    else:
        print "missing " + "".join(missing)
