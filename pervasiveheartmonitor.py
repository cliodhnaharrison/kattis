import sys

people = sys.stdin.read().split("\n")[:-1]

for person in people:
    person = person.split()
    name = []
    heart = []
    for value in person:
        if value[0].isalpha():
            name.append(value)
        else:
            heart.append(value)
    heart = [float(x) for x in heart]
    average = sum(heart) / len(heart)
    print average, " ".join(name)
