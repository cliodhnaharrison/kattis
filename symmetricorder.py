import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
lines = line[0:-1]

count = 1
n = 0

for item in lines:
    if item[0] == "0":
        break

    elif item[0].isalpha() == False:

        old_n = n + 1
        n += int(item) + 1
        sets = lines[old_n:n]

        one_half = []
        other_half = []

        for i in range(0, n-1, 2):
            if i >= len(sets):
                break
            else:
                one_half.append(sets[i])

        for i in range(1, n-1, 2):
            if i >= len(sets):
                break
            else:
                other_half.append(sets[i])

        whole = one_half + other_half[::-1]
        print "SET " + str(count)
        for item in whole:
            print item
        count += 1
        sets = []
