keyboard = {'a': (1, 0), 'b': (2, 4), 'c': (2, 2), 'd': (1, 2), 'e': (0, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'i': (0, 7), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 'm': (2, 6), 'n': (2, 5), 'o': (0, 8), 'p': (0, 9), 'q': (0, 0), 'r': (0, 3), 's': (1, 1), 't': (0, 4), 'u': (0, 6), 'v': (2, 3), 'w': (0, 1), 'x': (2, 1), 'y': (0, 5), 'z': (2, 0)}
n = int(input())

for _ in range(n):
    word, m = input().split()
    m = int(m)
    answers = {}
    for _ in range(m):
        c = input()
        distance = 0
        for char, origin in zip(c, word):
            distance += (abs(keyboard[char][0] - keyboard[origin][0]) + abs(keyboard[char][1] - keyboard[origin][1]))
        if distance in answers.keys():
            answers[distance].append(c)
        else:
            answers[distance] = [c]
    for dist in sorted(answers):
        if len(answers[dist]) == 1:
            print (answers[dist][0], dist)
        else:
            for w in sorted(answers[dist]):
                print(w, dist)
