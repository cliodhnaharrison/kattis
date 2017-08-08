import sys

input = sys.stdin.read()
line = input.split("\n")
line = line[:-1]

cases = []
output = []
animals = {}
count = 1
animals_counts = []

for item in line:
    if item[0].isalpha() == False:
        index = line.index(item)
        cases.append(line[:index])
        line = line[index+1:]

for item in cases:
    if len(item) == 0:
        continue
    else:
        for animal in item:
            animal = animal.split()
            if animal[-1].lower() in animals.keys():
                animals[animal[-1].lower()] += 1
            else:
                animals[animal[-1].lower()] = 1
        output.append("List " + str(count) + ":")
        for key in animals.keys():
            string = str(key) + " | " + str(animals[key])
            animals_counts.append(string)
        for item in sorted(animals_counts):
            output.append(item)
        animals = {}
        count += 1
        animals_counts = []

for item in output:
    print item
