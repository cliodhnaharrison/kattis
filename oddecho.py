n = int(input())
words = [input() for _ in range(n)]
for word in words[::2]:
    print(word)
