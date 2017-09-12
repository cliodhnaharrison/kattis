import sys

inputs = sys.stdin.read().split("\n")[:-1]

prices = [int(x) for x in inputs[0].split()]
inputs = inputs[1:]

parking = {}

for i in range(len(inputs)):
    truck = [int(x) for x in inputs[i].split()]
    for j in range(truck[0], truck[1]):
        if j in parking:
            parking[j].append(i)
        else:
            parking[j] = [i]

price = 0

for key in parking:
    price += len(parking[key]) * prices[len(parking[key]) - 1]

print (price)
