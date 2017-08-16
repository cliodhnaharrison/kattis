import sys
from collections import defaultdict

results = defaultdict(lambda: 0)

votes = sys.stdin.readlines()[:-1]

for vote in votes:
    results[vote] += 1

sorted_voted = sorted(list(results.items()), key=lambda z: z[1], reverse=True)

if len(sorted_voted) == 1 or (sorted_voted[0][1] != sorted_voted[1][1]):
    print sorted_voted[0][0]
else:
    print "Runoff!"
