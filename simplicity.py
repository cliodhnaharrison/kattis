s = input()
unique_letters = set(s)
counts = []
for letter in unique_letters:
    counts.append(s.count(letter))
counts = sorted(counts)
if len(unique_letters) < 3:
    print ("0")
else:
    print(sum(counts) - sum(counts[-2:]))
