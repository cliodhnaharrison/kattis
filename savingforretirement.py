import sys

inputs = sys.stdin.read()
inputs = inputs.strip("\n")
b, br, bs, a, asav = map(int, inputs.split())

total_bs = (br - b) * bs
total_as = 0

while total_as <= total_bs:
    a += 1
    total_as += asav

print a
