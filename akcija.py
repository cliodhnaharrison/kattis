import sys

books = sorted(sys.stdin.read().split("\n")[1:-1], key=int, reverse=True)

basket = ([books[i:i + 3] for i in range(0, len(books), 3)])

total = 0

for item in basket:
    item = [int(x) for x in item]
    if len(item) == 3:
        total += (sum(item) - min(item))
    else:
        total += sum(item)

print (total)
