import sys

inputstd = sys.stdin.read()
line = inputstd.strip("\n")

cs = line.count("C")
gs = line.count("G")
ts = line.count("T")

extra = 0
cards = [cs, gs, ts]
if 0 not in cards:
	extra = min(cards)

result = cs**2 + gs**2 + ts**2 + extra*7

print (result)
