t = int(input())

for i in range(t):
    n = int(input())
    ropes = input().split()
    red = []
    blue = []
    answer = 0
    for r in ropes:
        if "R" in r:
            red.append(r[:-1])
        else:
            blue.append(r[:-1])
    if len(red) == 0 or len(blue) == 0:
        answer = 0
    else:
        red = sorted([int(x) - 1 for x in red], reverse=True)
        blue = sorted([int(x) - 1 for x in blue], reverse=True)
        min_len = min(len(blue), len(red))
        for j in range(min_len):
            answer += red[j] + blue[j]

    print ("Case #" + str(i+1) + ": " + str(answer))
