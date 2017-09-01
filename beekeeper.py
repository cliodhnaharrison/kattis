import operator

n = int(input())

doubles = ["aa", "ee", "ii", "oo", "uu", "yy"]

while n != 0:
    words = []
    for _ in range(n):
        words.append(input())
    counts = {}
    for word in words:
        counts[word] = 0
        for vowel in doubles:
            counts[word] += word.count(vowel)
    v = list(counts.values())
    k = list(counts.keys())
    print (k[v.index(max(v))])
    n = int(input())
