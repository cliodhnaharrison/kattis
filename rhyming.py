test_word = input()
n = int(input())

rhyming = []

for _ in range(n):
    rhyming.append(input())

m = int(input())

phrases = []

for _ in range(m):
    phrases.append(input())

rhyming = [x.split() for x in rhyming]
phrases = [x.split()[-1] for x in phrases]

truths = []

for rhy in rhyming:
    for r in rhy:
        if r == test_word[-len(r):]:
            truths.append(rhy)
            break

rhymes = set([item for sublist in truths for item in sublist])

for p in phrases:
    match = False
    for r in rhymes:
        if r == p[-len(r):]:
            match = True
    if match:
        print ("YES")
    else:
        print ("NO")
