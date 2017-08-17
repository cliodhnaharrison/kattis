import sys

statement = sys.stdin.read().split("\n")[:-1]

m, n = map(int, statement[0].split())

words = statement[1:m+1]

costs = {}
for word in words:
    word = word.split()
    costs[word[0]] = int(word[1])

statement = statement[m+1:-1]
statement = " ".join(statement)
statement = statement.split(".")
for s in statement:
    total = 0
    if s == ".":
        continue
    else:
        line = s.split()
        for word in line:
            if word in costs:
                total += costs[word]
    print total
