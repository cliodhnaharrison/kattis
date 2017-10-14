n = int(input())

b = input()
paths = {}
while b != "-1":
    b = [int(x) for x in b.split()]
    paths[b[0]] = b[1:]
    b = input()

answer = [n]
ground = False

while not ground:
    found = False
    for i in paths:
        if n in paths[i]:
            answer.append(i)
            n = i
            found = True
        else:
            continue
    if not found:
        ground = True

print (" ".join([str(x) for x in answer]))
