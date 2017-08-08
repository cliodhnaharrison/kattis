import sys

input = sys.stdin.read()
line = input.strip("\n")

line1 = ["."]
line2 = ["."]
line3 = ["#"]
line4 = ["."]
line5 = ["."]

for i in range(len(line)):
    if (i+1) % 3 == 0 and i != 0:
        line1.append(".*..")
        line2.append("*.*.")
        line3.append("*." + str(line[i]) + ".*")
        line4.append("*.*.")
        line5.append(".*..")

    else:

        line1.append(".#..")
        line2.append("#.#.")
        if (i+2) % 3 == 0 and (i+1) in range(len(line)):
            line3.append("." + str(line[i]) + ".")
        else:
            line3.append("." + str(line[i]) + ".#")
        line4.append("#.#.")
        line5.append(".#..")


print "".join(line1)
print "".join(line2)
print "".join(line3)
print "".join(line4)
print "".join(line5)
