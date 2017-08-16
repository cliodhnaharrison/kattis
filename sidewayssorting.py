r, c = map(int, input().split())

final = []

while r != 0:
    words = []

    for j in range(r):
        s = input()
        i = 0
        for i in range(c):
            if j == 0:
                words.append(s[i])
            else:
                words[i] += s[i]

    words = sorted(words, key=lambda L: (L.lower(), L))
    out = []
    biggest = max(len(item) for item in words)
    for i in range(biggest):
        for item in words:
            if len(item) > i:
                out.append(item[i])
    composite_list = [out[x:x+c] for x in range(0, len(out),c)]

    for item in composite_list:
        final.append("".join(item))
    final.append("")

    r, c = map(int, input().split())

for item in final:
    print (item)
