n = int(input())

values = [int(x) for x in input().split()]
answers = []

for val in values:
    ans = 0
    for i in range(8):
        ans |= ((val ^ ans) & 2 ** i) * 2
    answers.append(str((ans // 2)))

print (" ".join(answers))
