import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", " ")
values = line.split(" ")
values = values[:-1]

people = int(values[0])
chicken = int(values[1])

if people > chicken:
    need = people - chicken
    if need > 1:
        print "Dr. Chaz needs", str(need), "more pieces of chicken!"
    else:
        print "Dr. Chaz needs", str(need), "more piece of chicken!"
else:
    left = chicken - people
    if left > 1:
        print "Dr. Chaz will have", str(left), "pieces of chicken left over!"
    else:
        print "Dr. Chaz will have", str(left), "piece of chicken left over!"
