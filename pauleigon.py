import sys

inputstd = sys.stdin.read()
values = inputstd.strip("\n")
values = values.split()

servers = ["paul", "opponent"]
result = 0
n = int(values[1])
m = int(values[2])
p = int(values[0])

nm = n + m
result  = int((float(nm)/p) % 2)
print (servers[result])
