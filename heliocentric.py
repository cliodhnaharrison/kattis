import sys

inputs = sys.stdin.read().split("\n")[:-1]

for i in range(len(inputs)):
    earth, mars = map(int, inputs[i].split())
    if earth == mars:
        print ("Case " + str(i+1) + ": 0")
    else:
        count = 0
        while earth != mars:
            count += 1
            earth += 1
            mars += 1
            if earth == 365:
                earth = 0
            if mars == 687:
                mars = 0
        print ("Case " + str(i+1) + ": " + str(count))
