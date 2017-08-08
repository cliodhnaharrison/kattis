import sys

line = sys.stdin.read()
line = line.strip("\n")
line = line.split()

vowels = ['a', 'e', 'i', 'o', 'u']
words = []

for word in line:
    word = list(word)
    for i in range(len(word) - 1):
        if i > (len(word) - 1):
            break
        if word[i] in vowels:
            del word[i+1]
            del word[i+1]
        i+= 1
    words.append(word)

words = ["".join(word) for word in words]
print " ".join(words)
