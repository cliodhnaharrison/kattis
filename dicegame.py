import sys

input = sys.stdin.read()
line = input.split("\n")
line = line[:-1]

gunnar = [int(x) for x in line[0].split()]
emma = [int(x) for x in line[1].split()]

g_count = 0
for low, high in zip(gunnar[::2], gunnar[1::2]):
    g_count += ((low + high) / 2.0)

e_count = 0
for low, high in zip(emma[::2], emma[1::2]):
    e_count += ((low + high) / 2.0)

if e_count > g_count:
    print "Emma"
elif g_count > e_count:
    print "Gunnar"
else:
    print "Tie"
