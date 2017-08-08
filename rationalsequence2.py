import sys

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[1:-1]

for item in lines:
    root = ["1/1"]
    p = 1
    q = 1
    n = item.split()[0]
    item = item.split()[1]
    count = 1
    while count < 10:
        if root[-1] == item:
            print count
            break
        root.append(str(p) + "/" + str(p + q))
        q = p + q
        root.append(str(p + q) + "/" + str(q))
        p = p + q
        count += 1
    print root

#left child of p/q  is p/(p+q).
#The right child of label p/q is (p+q)/q.
