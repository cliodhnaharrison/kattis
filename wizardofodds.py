n, k = map(int, input().split())

for _ in range(k):
    n = n / 2

if n <= 1:
    print ("Your wish is granted!")
else:
    print ("You will become a flying monkey!")
