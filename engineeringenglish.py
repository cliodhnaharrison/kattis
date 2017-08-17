import sys

lines = sys.stdin.read().split("\n")[:-1]

seen = []

for line in lines:
    words = line.split()
    output = []
    for word in words:
        wordlower = word.lower()
        if wordlower in seen:
            output.append(".")
        else:
            output.append(word)
            seen.append(wordlower)
    print " ".join(output)
