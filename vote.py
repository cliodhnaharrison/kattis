t = int(input())

for _ in range(t):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    total = sum(votes)
    win = max(votes)
    if votes.count(win) > 1:
        print ("no winner")
    elif win > total / 2:
        print ("majority winner " + str(votes.index(win) + 1))
    else:
        print ("minority winner " + str(votes.index(win) + 1))
