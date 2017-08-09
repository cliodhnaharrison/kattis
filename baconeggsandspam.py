import sys

input = sys.stdin.read()
lines = input.split("\n")
n = lines[0]
lines = lines[1:-1]


food = {}
for item in lines:
    if item[0].isalpha() == False:
        for item in sorted(food.keys()):
            print item, " ".join(sorted(food[item].split()))
        print " "
        if item[0] == "0":
            break
        food = {}
    else:
        item = item.split()
        person = item[0]
        for food_item in item[1:]:
            if food_item not in food:
                food[food_item] = person
            else:
                food[food_item] += " " + person
